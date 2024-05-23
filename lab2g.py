#!/usr/bin/env python3

#Author = Prabin Acharya
#Author ID: 100706225
#Date Created: 2024/05/22

import sys

#Creating a variable to store number of arguments.
NA = len(sys.argv)

if NA == 1:
    timer = 3
    while timer != 0:
        print(timer)
        timer = timer - 1

elif NA == 2:
    timer = int(sys.argv[1])
    while timer !=0:
        print(timer)
        timer = timer -1

print('blast off!')
