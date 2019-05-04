from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import mopac
import distance

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    resp = MessagingResponse()
    
    current_toll = mopac.get_specific_toll('sb: parmer to 5th/cvz')
    time_saved = distance.calc_time_saved()

    resp.message("Hey Hannah! Toll rate to get home is $" + str(current_toll) + " and will save you " + str(time_saved) + " minutes.")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
