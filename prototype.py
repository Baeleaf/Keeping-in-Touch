#!/usr/bin/env python

''' A contact the user wishes to keep in contact with via KITKAT. Contacts have the following properties:

Attributes:
    name: A string representing the contact's name.
    phone_number: A 10 digit integer representing the contact's phone number.
    notes: A string representing the user's notes about the contact.
    date_Last_Contacted: A datetime object representing the date and time since the user last contacted the contact.
    time_Since_Contacted: a datetime object representing the count-up of the time since the user last contacted the contact.
'''

import datetime
import time



def main(db):

    print("Welcome to the KITKAT prototype!\n1.New Entry\n2.Update\n3.View\n4.Exit")

    while True:
        userInput = raw_input("Enter your option: ")
        if userInput == '1':
            entry(db)
            printMenu()
        elif userInput == '2':
            print "You picked 'Update'"
            printMenu()
        elif userInput == '3':
            print db
            printMenu()
        elif userInput == '4':
            print("Exited.")
            saveToFile(db)
        else:
            print("\nError\n")
            time.sleep(1)
            print("Enter proper choice (1-4)")
            printMenu()


def init():
    db = []
    with open("db.txt") as f:
        for line in f:
            db.append(line)
    db = [x.strip() for x in db]

    print("printing db...")
    print(str(db))
    # main(db)

def update():
    pass

def saveToFile(db):
    f = open("db.txt","w")
    for ls in db:
        for item in ls:
            f.write(item + " ")
        f.write("\n")
    exit()

def entry(db):
    contact = []
    contact.append(raw_input("Who have you last contacted? "))
    contact.append(raw_input("Notes: "))
    contact.append(str(datetime.datetime.now()))
    contact.append(str(datetime.datetime.now()))
    # datetime.strptime(var,'%Y-%m-%d %H:%M:%S.%f') brings it back
    db.append(contact)

def printMenu():
    print("1.New Entry\n2.Update\n3.View\n4.Exit")

init()
