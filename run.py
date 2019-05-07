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

    if(time_saved == '0'):
        msg = "Don't take the toll, it won't save you any time and will cost you " + \
            current_toll + "."
    elif(time_saved == '1'):
        msg = "Hey! Toll rate to get home is " + current_toll + \
            " and will save you " + time_saved + " minute."
    else:
        msg = "Hey! Toll rate to get home is " + current_toll + \
            " and will save you " + time_saved + " minutes."

    resp.message(msg)
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
