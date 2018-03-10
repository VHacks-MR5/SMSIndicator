# SMSIndicator

> Indicates names, ages, gender, etc in SMS
----
### How It Work:
The Msg get received from **_Twilio_** API and saved locally in a file named by the sender phone number (using phone number as it won't be duplicated with anther person unlike names) then SMS Indicator parse through the msg file and retrieve important information listed [here](##) and send it to Database linking it to person photo then start matching between photos and last names to show relatives potentially receive information about them.

# #
* Indecator Detects:
    + [X] First Name
    + [X] Last Name
    + [ ] Nickname..etc (what yu worte as names)
    + [X] Countries (aka locality we love techinical language here)
    + [X] Gender
    + [X] Age
    + [ ] Locality
    + [ ] nationality
    + [ ] email
    + [X] phone

![Alt text](https://github.com/VHacks-MR5/SMSIndicator/blob/master/screens/Screen%20Shot%202018-03-10%20at%202.12.12%20PM.png)

* Indicators with some working funcitonality:
	/Feel in some whatever works to some degree /


-------
-------
-------

# Twilio

> Works for receiving the msg then --pass-it-to &rarr; SMSIndicator.



now I've finished: 
- code for reciving msg and print the msg on screen.
- to get public interface to connect witih local flask app  [ngrok](https://ngrok.com/downloadi) 

bug still need:
   - ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) `#f03c15` Alphanumeric Sender IDs cannot be used with trial accounts.
      + Can't activate it on my machine on trail version [*see sms section third sub*](https://support.twilio.com/hc/en-us/articles/223136107-How-does-Twilio-s-Free-Trial-work-)
   - update instead of printing the msg save it to file.
   - pass the msg file to indecator functions


#### some ideas:
- can send instant sms to the person tilling him we received his msg and will help *--Autromated--*
