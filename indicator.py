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
    return "name: " + name


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


def age(txt):
    return "Age(s): " + str([int(s) for s in txt.split() if s.isdigit()])


# text msg
msg = "hello, my name is Mustafa Jamal, male and lives in @Egypt!!! 21 yrs"

# functions Testing
print(noPunctuations(msg))
print(isName(msg))
print(isCountry(msg))
print(gender(msg))
print(age(msg))
