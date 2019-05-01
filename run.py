from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message("This will give details about Mopac Toll.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
