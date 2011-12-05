#import MySQLdb 
import os
import math

class Mysql:
	
	def addUser(self,username,firstName,secondName):
		user = Student(username,firstName,secondName)
		return user
		
	def findUser(self,username,firstName,secondName):
		user = Student(username,firstName,secondName)
		return user
	
	
	"""self.connect = MySQLdb.connect(	host = "localhost",
	                                user = "06williamsona",
	                                passwd = "cat",
	                                db = "06williamsona")
	self.cursor = self.connect.cursor()
	
	def run(self,queryinfo):
		self.cursor.execute(queryinfo)
	"""
	
	
class Student:
	
	def __init__(self,username,firstName,secondName):
		self.username = username
		self.firstName = firstName
		self.secondName = secondName
	
username = "06williamsona"
firstName = "Ashley"
secondName = "Williamson"


user = Mysql().addUser(username,firstName,secondName)

for attr, value in user.__dict__.iteritems():
	if attr == ("username"):
		attr = "Username"
		
	elif attr ==("firstName"):
		attr = "First Name"
	else:
		attr = "Second Name"
	print attr + ": " + value
	
	
"""v ={"username":"Username: {}", "firstname":"Firstname: {}", "secondname":"Second name: {}"}


for attr in ["username", "firstname","secondname"]:
    print v[attr].format(self.attr)
    

print(v)


"""
	
