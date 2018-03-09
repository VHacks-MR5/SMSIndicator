# text msg
msg = "hello, my name is Mustafa Jamal, mail and lives in Egypt"


"""
@:param text string 
@:return the name in the msg
"""
def isName(txt):
    name = ""
    txtList = txt.split()
    for word in txtList:
        if word[0].isupper():
            name += word + " "
    return "name: " + name

# print(isName(msg))


"""
@:param
@:return

"""