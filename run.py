from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import mopac
import distance
import messaging
import config

app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    body = request.values.get('Body', None)
    resp = MessagingResponse()

    # Determine which direction (northbound/southbound) user is asking for
    intent = messaging.process_intent(body)

    # Call Mopac and Google Maps API endpoints for appropriate direction
    if intent == 'n':
        current_toll = mopac.get_specific_toll('nb: cvz to 183')
        time_saved = distance.calc_time_saved(
            config.HOME_ADDRESS, config.WORK_ADDRESS)
    elif intent == 's':
        current_toll = mopac.get_specific_toll('sb: 2222 to 5th/cvz')
        time_saved = distance.calc_time_saved(
            config.WORK_ADDRESS, config.HOME_ADDRESS)
    else:
        resp.message('Please reply which direction you are heading on MoPac.')
        return(str(resp))

    # Generate response message
    msg = messaging.build_message(intent, time_saved, current_toll)

    resp.message(msg)
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
