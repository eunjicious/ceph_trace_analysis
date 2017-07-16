#! /usr/bin/python2.7
import sys
import re
#
class Obj:
	def __init__(self):
		self.name = ""
		self.data_len= 0
		self.oh_len = 0
		self.xattrs = [{}]
		self.omap = [{}]


class Coll:
	def __init__(self):
		self.name =  ""
		self.xattrs = [{}]
		self.obj = [Obj] 

def change_name(Coll):
	coll.name="new name"

#### main function 
if __name__ == "__main__":
	print("I am main function")
	coll = Coll()
	coll.name = "coll0"  
	print(coll.name)	
	change_name(coll)
	print(coll.name)



