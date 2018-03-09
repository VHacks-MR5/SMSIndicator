# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "ACfeda866b73a7220b7e52d22485bb6b39"
auth_token = ""

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+",
    from_="+18329815670",
    body="Hello there!")