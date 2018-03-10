"""
RECEIVE AND REPLY TO SMS AND MMS MESSAGES
SDK Version 6.x

Author: Mustafa Jamal
March 9, 2018
"""

from flask import Flask, request, redirect
from twilio import twiml


app = Flask(__name__)

# use route decorator to till our app to use sms function when ever sms send over POST request
@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']   # The number of msg
    msgBody = request.form['Body']  # Body of msg

    # print the msg
    print("Phone Number" + number)
    print("Content" + msgBody)

if __name__ == "__main__":
    app.run(debug=True)
