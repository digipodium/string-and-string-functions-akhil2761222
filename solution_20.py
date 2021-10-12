my_string = input('please enter your string: ')
for i in my_string:
    upr = i.isupper()
    if upr is True:
        print('found')

        break
