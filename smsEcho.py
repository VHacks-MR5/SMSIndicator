"""
This Will Echo the Sender SMS Back to his phone number
SDK Version 6.x

Author: Mustafa Jamal
April 28, 2018
"""


from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message("Vinculum received your msg successfully! ☮︎")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)