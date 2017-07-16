#!/usr/bin/env python

import json
import os
		
def addFirstUser(name, phone, color):
	data = {
		name: {
			'Phone' : phone,
			'Color' : color
			}
	}

	with open('newData.json', 'w') as f:
		json.dump(data, f)

def addUser(name, phone, color):
	datas = {
		name: {
			'Phone' : phone,
			'Color' : color
		}
	}

	with open('newData.json') as f:
		data=json.load(f)

	data.update(datas)

	with open('newData.json', 'w') as f:
		json.dump(data, f)

def addProperty(user, key, value):
	datad = {
		key:value
	}

	with open('newData.json') as f:
		data=json.load(f)

	data[user].update(datad)

	with open('newData.json', 'w') as f:
		json.dump(data, f)

def readUsersProperties(user):
	with open('newData.json', 'r') as f:
		data=json.load(f)

		userData=(data[user])

	for key, value in userData.items():
			print(key + ": " + value)

def readSpecificProperty(user,property):
	with open('newData.json', 'r') as f:
		data=json.load(f)

	print(data[user][property])

def readContactList():
		with open('newData.json', 'r') as f:
			data=json.load(f)

		for key, value in data.items():
				print(firstkey + " " + key + ": " + value)

if os.path.exists("newData.json")==False or os.stat("newData.json").st_size==0:
	print("You haven't added a user yet! Let's add your first user!")
	addFirstUser(name=raw_input("What is the user's name?\n"), phone=raw_input("What is the user's phone nubmer?\n"), color=raw_input("What is the users color?\n"))

choice=raw_input("What do you want to do?\n 1. Add a user\n 2. Add a property to a user.\n 3. Read a user's properties.\n 4. Read a specific property from a user\n")
if "add" in choice and "user" in choice or choice=="1":

	addUser(name=raw_input("What is the user's name?\n"), phone=raw_input("What is the user's phone number?\n"), color=raw_input("What is the user's color?\n"))
	
if "add" in choice and "property" in choice or choice =="2":
	addProperty(user=raw_input('What user do you want to add to? \n'),key=raw_input('What property do you want to add? \n'),value=raw_input('What value do you want to add to the property?\n'))

if "read" in choice and "user" in choice or choice == "3":
	readUsersProperties(user=raw_input('What user do you want to read from? \n'))

if "read" in choice and "property" in choice or choice =="4":
	readSpecificProperty(user=raw_input('What user do you want to read from? \n'), property=raw_input('What property do you want to see? \n'))