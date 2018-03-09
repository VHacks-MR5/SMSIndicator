import string

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
    return "Name: " + name


"""
This Function to check the countries in the msg
@:param
@:return
"""
def isCountry(txt):
    countryFound = ""
    noPunTxt = (noPunctuations(txt))
    txtList = noPunTxt.split()
    with open("countries") as f:
        countryList = f.read().splitlines()

    for country in countryList:
        if country in txtList:
            countryFound += country

    return "Country: " + countryFound


"""
Returns the Gender if mentioned 
@:param String
@:return the Gender from the msg
"""
def gender(txt):
    genders = ""
    clearTxt = noPunctuations(txt)
    lowerTxt = clearTxt.lower()
    if "male" in lowerTxt:
        genders += "Male"
    if "female" in lowerTxt:
        genders += "Female"

    return "Gender(s): " + genders


"""
Returns the Age number as a string from text msg
numbers up to 3 boxes only
else it won't return that
@:param String
@:return numbers in it as List 
"""
def age(txt):
    numbersList = [int(s) for s in txt.split() if s.isdigit()]
    for ele in numbersList:
        if ele < 333:
            return "Age: " + str(ele)
    return "No Age In the Msg"


"""
Returns the phone number as a string from text msg
else it won't return that
@:param String
@:return numbers in it as List 
"""
def phone(txt):
    numbersList = [int(s) for s in txt.split() if s.isdigit()]
    for ele in numbersList:
        if ele > 999:
            return "Phone no.: " + str(ele)
    return "No Phone Number"


# text msg
msg = "hello, my name is Mustafa Jamal, male and lives in @Egypt!!! 21 yrs phone no. 123456789"

# functions Testing
print(noPunctuations(msg))
print(isName(msg))
print(isCountry(msg))
print(gender(msg))
print(age(msg))
print(phone(msg))
