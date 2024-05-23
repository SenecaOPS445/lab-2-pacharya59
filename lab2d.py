#!/usr/bin/env python3

import sys

#Storing the number of arguments into a variable called collection.
collection = len(sys.argv)

#If not provided two argumentss, it will display usage message to the user.
if collection != 3:
    print('Usage: ' + sys.argv[0] + ' name ' + 'age')
    sys.exit()
else :
    name = sys.argv[1]
    age = sys.argv[2]
    print('Hi ' + name + ', you are ' + str(age) + ' years old.')
