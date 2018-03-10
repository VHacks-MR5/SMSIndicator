# SMSIndicator

> Indicates names, ages, gender, etc in SMS

* Soon wnough it should detect:
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
   - ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) `#f03c15`Alphanumeric Sender IDs cannot be used with trial accounts.
      + Can't activate it on my machine on trail version [*see sms section third sub*](https://support.twilio.com/hc/en-us/articles/223136107-How-does-Twilio-s-Free-Trial-work-)
   - update instead of printing the msg save it to file.
   - pass the msg file to indecator functions


#### some ideas:
- can send instant sms to the person tilling him we received his msg and will help *--Autromated--*
