import re

def displaymatch(match):
    if match is None:
        return "Invalid Email Address"
    return _user #"Valid Email Address" #'<Match: %r, groups=%r>' % (match.group(), match.groups())

email = re.compile(r"^\b[a-zA-Z0-9]+@[a-z]+.[a-z]\b")

# _user = input("Enter A Username to check : ")

# displaymatch(email.match(_user))

