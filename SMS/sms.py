
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'XXX'
auth_token = 'XXX'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                    body="This is Anna, sending the first SMS through Twillio",
                    from_='+XXXXXXXXXXX',
                    to='+1XXXXXXXXXX'
                )

print(message.sid)
