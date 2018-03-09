import re
import string


# text msg
msg = "hello, my name is Mustafa Jamal, mail and lives in Egypt"


"""
Clear Punctuations
@:param String
@:return Clear string from punctuations
"""
def noPunctuations(txt):
    return txt.translate(str.maketrans('','',string.punctuation))


"""
This Function to names the countries in the msg,
@:param text string 
@:return the name in the msg
"""
def isName(txt):
    name = ""
    clearTxt = noPunctuations(txt)
    txtList = clearTxt.split()
    with open("countries") as f:
        countryList = f.read().splitlines()
    for word in txtList:
        if word[0].isupper() and word not in countryList:
            name += word + " "
    return "name: " + name

print(isName(msg))


"""
This Function to check the countries in the msg
@:param
@:return
"""
def isCountry(txt):
    countryFound = ""
    txtList = txt.split()
    with open("countries") as f:
        countryList = f.read().splitlines()

    for country in countryList:
        if country in txtList:
            countryFound += country

    return "Country: " + countryFound

print(isCountry(msg))
