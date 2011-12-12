#Ashley Williamson 8th December 2011



import MySQLdb
import os
import sys
import math
import getpass

class Mysql:
	
	def addUser(self,username,firstName,secondName): #Add user method
		user = Student(username,firstName,secondName) # New object called user, so i can reference the things i've just put into it like user.username
		return user #Has to return the object, derrr.
		
	def findUser(self,username,firstName,secondName): #Find User method
		user = Student(username,firstName,secondName) #new object called user, with the information of the student. Needs work, will use a query to find the username specified and return values dependant on what it finds.
		return user
	
	def __init__(self):
		
		try: #Try to connect to the database
			self.connect = MySQLdb.connect(host = "localhost",user = "06williamsona", passwd = "cat",db = "06williamsona" )

		except MySQLdb.Error, e: #If it cannot, for instance one of the params is invalid, or incorrect, it will throw the error	
			print "Error %d: %s" % (e.args[0], e.args[1]) #Catch both arguements to the error, and print it out to the user using %d and %s
			sys.exit(1)
			
		try: #Try to create the cursor object, required for queries after connection has been made
			self.cursor = self.connect.cursor()
			

		except MySQLdb.Error, e: 	#Same error catching as above
			print "Error %d: %s" % (e.args[0], e.args[1])

	def run(self): #A method which would run queries for me, so i could have done mysql().run(BLARGH)
		try: #Again try the query, and return a error with the errors arguments 
			self.cursor.execute("SELECT firstName FROM testforDj")
					
		except MySQLdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])

	
		while(1):

			row = self.cursor.fetchone()

			for i in int(self.cursor.rowcount):
				print row[i]
				print "Number of rows returned: %d" % self.cursor.rowcount

			if row == None:
				break
	
	
	
class Student: #Student Class to hold all of the selected users information.	
	def __init__(self,username,firstName,secondName): #Init method automatically invoked when creating a new class object/instance
		self.username = username #So define all my local variables, and attribs which i can access later via the object name from mysql which was user, then .the atrrib.
		self.firstName = firstName
		self.secondName = secondName
	
def getMoreInfo(username,password): #It takes the username and password, the beginning information from the login method
	firstName = raw_input("What is your firstName? ") #Assigns firstName and secondName to some raw_inputs
	secondName = raw_input("What is your secondName? ")
	
	user = mysqlObj.addUser(username,firstName,secondName) # Creates the user object, since addUser returns the object, user now becomes the user object. Snazzy no?
	
	for attr, value in user.__dict__.iteritems(): #LOVELY FOR LOOP! It basically goes through the attrib names like username, firstName and then the values for each, by iterating through each in the user object
		#Rather hacky way, normally used in debuggers, but it'll suffice
		
		if attr == ("username"): #Some if statements so formatting looks nice, instead of firstName Ashley, it's First Name: Ashley
			attr = "Username" #Now assign the attrib of this iteration a fancier looking name!
		
		elif attr ==("firstName"):
			attr = "First Name"
		else:
			attr = "Second Name"
			
		print attr + ": " + value.capitalize() #The print statement to print the attr which we made fancier, then have a nice : and then the value! Having it add : here instead of above says 1 char per string!
	

def checkUser(username,password): # function responsible for just checking the information (this would be against the db, but for now it's just static info login information) and returns 1 or -1 depandant on the result!
	if (username.isalnum())and(username.isalnum()):
		if (username == "06williamsona") and (password == "ohyeah"): #If both fields match we'll return 1 saying that yes it's valid,
			return 1 #see 
		else: #otherwise
			print "Incorrect" #We'll tell them it's wrong so they know what's going on
			return -1 #And we'll throw -1, so the method login knows that i needs to ask them again!
	else:
		print "You have invalid characters within your username and/or password, please try again."
		return -1

def exit():
	print "Thankyou for using the school system"
	if(MysqlObj.commit()): #Commit changes to the database
		print "Changes commited to the database"
	if(MysqlObj.cursor.close()): #Close the cursor object
		print "Cursor Closed"
	if(MysqlObj.connect.close()): #Close the mysql conenction
		print "Connection Closed"
	


mysqlObj = Mysql()

if(mysqlObj):

	invalid = True

	while invalid == True:

		username = raw_input("Username: ") #Initial call for information
		password = getpass.getpass()

		if checkUser(username, password) >= 1:
			invalid = False
			print "Invalid is now equal to,",str(invalid)
			#getMoreInfo(username,password)

			#query = raw_input("Please enter a query: ")
			mysqlObj.run()



	## CHECKS OUT, DO SOME MORE STUFF
