from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import mopac

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    resp = MessagingResponse()
    
    current_toll = mopac.get_specific_toll('sb: parmer to 5th/cvz')

    resp.message("Current SB Mopac Toll is $" + str(current_toll))
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
