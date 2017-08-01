#!/usr/bin/env python

'''
Author: Kwame Robertson

Date: 7/19/17

Description: This is a prototype of the KITKAT application that serves a record-keeping program to keep in touch with contacts and continue to develop networking relationships. This program stores information on the user's contacts and allows the user to add, update, and view any information.

Dependencies: python-dateutil
'''

import datetime, time, json, os
import dateutil.relativedelta

# Helper Functions

def printMenu():
	print("1.New Entry\n2.Update\n3.View\n4.Save and Exit")

def saveToFile(contactList):	
	with open('db.json', 'w') as f: # Saves edited data to .json file
		json.dump(contactList, f)
	exit()

def init():
	if os.path.exists("db.json") != False and os.stat("db.json").st_size != 0: # if file exists with information
		with open('db.json') as f: # Load previously saved data from .json file
			contacts = json.load(f)
	else:
		contacts = {}
	main(contacts)

def refreshTime(inputTime):
	oldTime = datetime.datetime.strptime(inputTime,'%Y-%m-%d %H:%M:%S.%f') 
	newTime = datetime.datetime.now()

	# finalTime = newTime - oldTime
	# return "It has been %d days." % (finalTime.days)

	finalTime = dateutil.relativedelta.relativedelta (newTime, oldTime)
	return "It has been %d years, %d months, %d days, %d hours, and %d minutes." % (finalTime.years, finalTime.months, finalTime.days, finalTime.hours, finalTime.minutes)

def sanitizeUpdateInput(contactList, nameInput, propInput, valueInput):
	userInput = [nameInput, propInput, valueInput, False]
	nameExists = False
	propExists = True
	if propInput.lower() not in 'Last Contacted'.lower() and propInput.lower() not in 'How Long'.lower():
		for k, v in contactList.items(): # loops through names (string, dict)
			if nameInput == "" or propInput == "":
				break

			if nameInput.lower() in k.lower():
				nameExists = True
				userInput[0] = k
			else:
				continue

			for key, value in v.items(): # loops through values (string, string)
				if propInput.lower() in key.lower() or key.lower() in propInput.lower():
					propExists = True
					userInput[1] = key
	else:
		print "\nYou may not edit these properties."
		time.sleep(1)

	if nameExists and propExists:
		userInput[3] = True
		return userInput
	else:
		return userInput

# Main Functions

def entry(contactList, name, phone, notes):
	# Initialize an empty dictionary filled with parameters
	contacts = {
		name: {
			'Phone': phone,
			'Last Contacted': str(datetime.datetime.now()),
			'How Long': "It has been 0 years, 0 months, 0 days, 0 hours, and 0 minutes.",
			'Notes': notes
			}
	}
	
	contactList.update(contacts) # Merge previous dictionary with new dictionary


def update(contactList, user, key, value):
	# Initialize an empty dictionary filled with parameters
	mergeMe = {
		key: value
	}
	
	contactList[user]['Last Contacted'] = str(datetime.datetime.now())
	contactList[user].update(mergeMe)


def view(contactList):
	if not contactList:
		print "\nThere doesn't seem to be anything here. Add a contact!\n"
		return

	for k, v in contactList.items(): # loops through names (string, dict)
		print('\n' + k)
		contactList[k]['How Long'] = refreshTime(contactList[k]['Last Contacted'])
		for key, value in v.items(): # loops through values (string, string)
			if key.lower() == 'Last Contacted'.lower():
					var = datetime.datetime.strptime(value,'%Y-%m-%d %H:%M:%S.%f').strftime("%B %d,%Y %H:%M:%S")
					print(key + ": " + var)
			else:
				print(key + ": " + value)
	print('\n')

def main(contacts):
	try:
		print("Welcome to the KITKAT prototype!\n1.New Entry\n2.Update\n3.View\n4.Exit")

		while True:
			userInput = raw_input("Enter your option: ")
			if userInput == '1':
				entry(contacts, name = raw_input("Who have you last contacted? "), phone = raw_input("Enter their phone number: "), notes = raw_input("Notes: "))
				print "\nEntry saved.\n"
				time.sleep(1)
				printMenu()
			elif userInput == '2':
				if not contacts:
					print "\nThere doesn't seem to be anything here. Add a contact!\n"
				
				else:
					updateInput = sanitizeUpdateInput(contacts, nameInput = raw_input("Who would you like to update? ").title(), propInput = raw_input("What would you like to change? ").title(), valueInput = raw_input("Edit below:\n"))
					
					if updateInput[3]:
						update(contacts, updateInput[0],updateInput[1],updateInput[2])
						print "\nEntry Updated.\n"
						time.sleep(1)
					else:
						print("\nThat name or property is not available. Please try again.\n")
						time.sleep(1)
	
				printMenu()
			elif userInput == '3':
				view(contacts)
				time.sleep(1)
				printMenu()
			elif userInput == '4':
				print("\nExited.\n")
				saveToFile(contacts)
			else:
				print("\nError\n")
				time.sleep(1)
				print("Please enter a proper choice (1-4)\n")
				printMenu()

	except KeyError:
		print("An unexpected error has occurred. Restarting the program. Please wait.")
		time.sleep(5)
		init()
init()