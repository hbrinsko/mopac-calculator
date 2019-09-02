from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import mopac
import distance
import messaging
import config
import sys
import pymongo


app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    body = request.values.get('Body', None)
    resp = MessagingResponse()

    # Get User information
    from_number = request.values.get('From')
    uri = config.MONGO_CONNECTION

    client = pymongo.MongoClient(uri)
    db = client.get_default_database()
    collection = db['mopac-calc']
    query = { "phone": from_number }

    user = collection.find_one(query)
    client.close()
    if user is None:
        msg = 'Unable to find commute information for: ' + str(from_number)
        resp.message(msg)
        return str(resp)

    print(user['phone'])

    # Determine which direction (northbound/southbound) user is asking for
    intent = messaging.process_intent(body)

    # Call Mopac and Google Maps API endpoints for appropriate direction
    if intent == 'n':
        current_toll = mopac.get_specific_toll(user['northToll'])
        time_saved = distance.calc_time_saved(
            user['home'], user['work'])
    elif intent == 's':
        current_toll = mopac.get_specific_toll(user['southToll'])
        time_saved = distance.calc_time_saved(
            user['work'], user['home'])
    else:
        resp.message('Please reply which direction you are heading on MoPac.')
        return(str(resp))

    # Generate response message
    msg = messaging.build_message(intent, time_saved, current_toll)

    resp.message(msg)

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
