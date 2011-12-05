#import MySQLdb 
import os
import math

class Mysql:
	
	def addUser(self,username,firstName,secondName): #Add user function
		user = Student(username,firstName,secondName) # New object called user, so i can reference the things i've just put into it like user.username
		return user #Has to return the object, derrr.
		
	def findUser(self,username,firstName,secondName): #Find User function
		user = Student(username,firstName,secondName) #new object called user, with the information of the student. Needs work, will use a query to find the username specified and return values dependant on what it finds.
		return user
	
	
	"""self.connect = MySQLdb.connect(	host = "localhost", # SQL Open a connection, lovely stuff, can't do on a windows atm, waiting for later.
	                                user = "06williamsona",
	                                passwd = "cat",
	                                db = "06williamsona")
					
	self.cursor = self.connect.cursor() #Cursor required to query le server
	
	def run(self,queryinfo): #A function which would run queries for me, so i could have done mysql().run(BLARGH)
		self.cursor.execute(queryinfo)
	"""
	
	
class Student: #Student Class to hold all of the selected users information.
	
	def __init__(self,username,firstName,secondName): #Init function, will always run when a new object of the class is made. __Init__ indicates in a special function.
		self.username = username #So define all my local variables, and attribs which i can access later via the object name from mysql which was user, then .the atrrib.
		self.firstName = firstName
		self.secondName = secondName
	

def login(): #Function for getting initial login information from the user
	
	username = raw_input("Please enter your username: ") #Initial call for information
	password = raw_input("Please enter your password: ")
	
	while checkUser(username,password) < 1: #Well if it's wrong, we've got to do it again, and i don't fancy recursion.
		username = raw_input("Please enter your username: ")
		password = raw_input("Please enter your password: ")
	else: #Well, if it's not less than 1 it must be right! so lets say they've logged in and pass it onto a function to get some more information to fill up out Student Object
		print "logged in"
		getMoreInfo(username,password)
		
def getMoreInfo(username,password): #It takes the username and password, the beginning information from the login function
	firstName = raw_input("What is your firstName? ") #Assigns firstName and secondName to some raw_inputs
	secondName = raw_input("What is your secondName? ")
	
	user = Mysql().addUser(username,firstName,secondName) # Creates the user object, since addUser returns the object, user now becomes the user object. Snazzy no?
	
	for attr, value in user.__dict__.iteritems(): #LOVELY FOR LOOP! It basically goes through the attrib names like username, firstName and then the values for each, by iterating through each in the user object
		
		if attr == ("username"): #Some if statements so formatting looks nice, instead of firstName Ashley, it's First Name: Ashley
			attr = "Username" #Now assign the attrib of this iteration a fancier looking name!
		
		elif attr ==("firstName"):
			attr = "First Name"
		else:
			attr = "Second Name"
			
		print attr + ": " + value #The print statement to print the attr which we made fancier, then have a nice : and then the value! Having it add : here instead of above says 1 char per string!
	

def checkUser(username,password): # Function responsible for just checking the information (this would be against the db, but for now it's just static info login information) and returns 1 or -1 depandant on the result!
	if (username == "06williamsona") and (password == "ohyeah"): #If both fields match we'll return 1 saying that yes it's valid,
		return 1 #see 
	else: #otherwise
		print "Incorrect" #We'll tell them it's wrong so they know what's going on
		return -1 #And we'll throw -1, so the function login knows that i needs to ask them again!
	
login() #Initial call to the function, as i always do!

#Random crap when testing attrib iterations
"""v ={"username":"Username: {}", "firstname":"Firstname: {}", "secondname":"Second name: {}"}


for attr in ["username", "firstname","secondname"]:
    print v[attr].format(self.attr)
    

print(v)


"""
	
