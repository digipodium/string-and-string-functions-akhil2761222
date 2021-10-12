text = '%p34@y!*-*!t68h#&on404'

alphanum = ""

for character in text:
    if character.isalnum():
        if character.isnumeric() is not True:
            alphanum += character


print(alphanum)