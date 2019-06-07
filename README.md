# MoPac Calculator
 [MoPac](https://www.mobilityauthority.com/traveler-info/open-roads/MoPac-Express) is an 11-mile variably-priced tolled express lane along MoPac between Cesar Chavez Street and Parmer Lane in Austin, TX.

> Those wanting to bypass traffic congestion have a choice to use the MoPac Express Lane. Drivers who prefer not to pay a toll can use the non-tolled lanes on MoPac.

This application allows the user to see how much time they can save by taking the MoPac Express Lane, along with providing the current toll rate for a specified direction (northbound vs southbound).


## Acquire API Keys
Before you can run this project, you will need to set up accounts with Twilio and Google and set up the following in config.py:

* `ACCOUNT_SID` : Your Twilio "account SID" - it's like your username for the Twilio API.  This and the auth token (below) can be found [on your account dashboard](https://www.twilio.com/user/account).
* `AUTH_NUM` : Your Twilio "auth token" - it's your password for the Twilio API.  This and the account SID (above) can be found [on your account dashboard](https://www.twilio.com/user/account).
* `TO_NUM` : A Twilio number that you own.  You can find a list of phone numbers you control (and buy another one, if necessary) [in the account portal](https://www.twilio.com/user/account/phone-numbers/incoming).
* `GOOGLE_KEY` : To use the Google Maps Embed API you must have an API key that is used to authenticate requests associated with [your project](https://developers.google.com/maps/documentation/embed/get-api-key).


## Setting up the Python Application
Assuming that before you begin, you will have [Python](http://www.python.org/) and [pip](http://www.pip-installer.org/en/latest/) installed on your system and available at the command line.

Install depenedencies:

```bash
pip install -r requirements.txt
```

Run the application using [ngrok](https://hackernoon.com/using-twilio-to-send-sms-texts-via-python-flask-and-ngrok-9874b54a0d3) or deploy with Google Cloud Platform:

```bash
gcloud app deploy
```

Run unit tests:
```bash
pytest test_messaging.py
```