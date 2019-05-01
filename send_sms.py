import config
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = config.account_sid
auth_token = config.auth_token
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     from_= config.from_num,
                     to= config.to_num
                 )

print(message.sid)
