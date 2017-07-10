#!/usr/bin/env python


''' A contact the user wishes to keep in contact with via KITKAT. Contacts have the following properties:

Attributes:
    name: A string representing the contact's name.
    phone_number: A 10 digit integer representing the contact's phone number.
    notes: A string representing the user's notes about the contact.
    date_Last_Contacted: A datetime object representing the date and time since the user last contacted the contact.
    time_Since_Contacted: a string(?) representing the count-up of the time since the user last contacted the contact.
'''

import datetime

db = []
#
# def init():
#     inFile = open("db.txt")
#     for line in inFile:
#         db.append(line)
#     inFile.close()
#     # UPDATE time_Since_Contacted VALUE HERE
#     main()


def main():

    print("Welcome to the KITKAT prototype!\n1.New Entry\n2.Update\n3.View\n4.Exit")

    while True:
        userInput = raw_input("Enter your option: ")
        if userInput == '1':
            entry()
            printMenu()
        elif userInput == '2':
            print "You picked 'Update'"
            printMenu()
        elif userInput == '3':
            print db
            printMenu()
        elif userInput == '4':
            print("Exited.")
            exit()
        else:
            print("Error\nEnter proper choice (1-4)")
            printMenu()


def update():


def entry():
    contact = {}
    name = raw_input("Who have you last contacted?")
    notes = raw_input("Have any notes?")
    contact.update({'Name': name, 'notes': notes, 'date_Last_Contacted': datetime.datetime.now(), 'time_Since_Contacted': datetime.datetime.now()})
    db.append(contact)

def printMenu():
    print("1.New Entry\n2.Update\n3.View\n4.Exit")

# init()
main()
