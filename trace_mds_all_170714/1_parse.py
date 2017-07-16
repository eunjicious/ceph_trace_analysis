#! /usr/bin/python2.7

import sys
import re

class Obj:
	def __init__(self, name):
		self.name = name
		self.data_len= 0
		self.omap_header_len = 0
		self.xattrs = [] ## {}
		self.omap = [] ## {}
		self.xattrs_len = 0
		self.omap_len = 0

class Coll:
	def __init__(self, name):
		self.name = name
		self.xattrs = [{}]
		self.obj = [] ## Obj
		self.xattrs_len = 0

class Colls:
	def __init__(self):
		self.coll = [] ## Col

colls = []

def debug_print(*args):
	return
#	print(args)


def fread(lfname):
	lfo = open(lfname, "r")
	return lfo.readlines()

def ftokenize(flines):
	token_list = []
	for fline in flines:
		token_list += re.split(' |"|"|,|:|\n', fline.replace(" ", "").rstrip())
		#token_list += re.split(' |"|"|,|:|\n', fline.replace(" ", "").rstrip())
	return filter(None, token_list)


def parse_get_name (token_list, i):
	name = ""	
	while i < len(token_list):
		token = token_list[i]
		debug_print ("parse_get_name : ", i, " ", token)

		if token == "data_len" or token == "xattrs":
			i -= 1
			break

		name = name + token + ":"
		i += 1
		
	return name, i
	


def parse_xattrs_len (token_list, i):
	open_cnt = 0
	tot_len = 0 

	while i < len(token_list):
		token = token_list[i]
		debug_print ("parse_xattrs_len : ", i, " ", token)

		if token == '[':
			open_cnt += 1
		elif token == "length":
			i += 1
			tot_len += int(token_list[i])
		elif token == ']':
			open_cnt -= 1

		####
		if open_cnt == 0:
			break
		i += 1 
	debug_print("parse_xattrs_len: ", tot_len, i)
	return tot_len, i

def parse_omap_len (token_list, i):
	open_cnt = 0
	tot_len = 0 

	while i < len(token_list):
		token = token_list[i]
		debug_print ("parse_omap_len : ", i, " ", token)

		if token == '[':
			open_cnt += 1
		elif token == "length":
			i += 1
			tot_len += int(token_list[i])
		elif token == ']':
			open_cnt -= 1

		####
		if open_cnt == 0:
			break
		i += 1 

	return tot_len, i

def parse_objects(token_list, i, my_coll):

	oid = 0
	open_cnt = 0

	while i < len(token_list):
		token = token_list[i]
		debug_print("parse_objects : ", i, " ", token)

		if (token == '['):
			open_cnt += 1

		elif (token == ']'):
			open_cnt -= 1

		elif (token == "name"):
			name, i = parse_get_name(token_list, i)
			my_coll.obj.append(Obj(name))
			oid = len(my_coll.obj) - 1

		elif (token == "data_len"):
			i += 1
			my_coll.obj[oid].data_len = token_list[i]

		elif (token == "omap_header_len"):
			i += 1
			my_coll.obj[oid].omap_header_len = int(token_list[i])

		elif (token == "xattrs"):
			i += 1
			my_coll.obj[oid].xattrs_len, i = parse_xattrs_len (token_list, i)

		elif (token == "omap"):
			i += 1
			my_coll.obj[oid].omap_len, i = parse_omap_len (token_list, i)
		else:
			pass
	
		if open_cnt == 0:
			break
		
		i += 1
	return i 


def parse_collections(token_list, i, my_colls):

	cid = 0
	open_cnt = 0

	while i < len(token_list):
		token = token_list[i]
		debug_print ("parse_collections : ", i, " ", token)

		if token == '[':
			open_cnt += 1
		elif token == ']':
			open_cnt -= 1
#		elif token == '{':
#			cid += 1
		elif token == "name": 
			name, i = parse_get_name(token_list, i)
			my_colls.coll.append(Coll(name))
			cid = len(my_colls.coll) - 1

		elif token == "xattrs":
			i += 1
			my_colls.coll[cid].xattrs_len, i = parse_xattrs_len (token_list, i)
		elif token == "objects":
			i += 1	
			i = parse_objects(token_list, i, my_colls.coll[cid])
		else:
			pass

		### 
		if open_cnt == 0:
			break
	
		i = i+1
	
	return i

def parse(token_list):
	i = 0
	csid = -1	

	while i < len(token_list):
		token = token_list[i]
		debug_print ("parse : ", i, " ", token)
		
		if token == "collections":
			colls.append(Colls())
			csid = len(colls) - 1
			i += 1
			i = parse_collections(token_list, i, colls[csid])
		
		i += 1
		
	debug_print (len(token_list))


def print_stat():
	#print(colls[0].coll[0].name)
	#print(len(colls))
	for cs in colls:
		for coll in cs.coll:
			for obj in coll.obj:
				print(coll.name + " " + 
					str(coll.xattrs_len) + " " +
					obj.name + " " +
					str(obj.data_len) + " " +
					str(obj.xattrs_len) + " " +
					str(obj.omap_header_len) + " " +
					str(obj.omap_len)
				)

######################
if len(sys.argv) < 2:
	print("Usage: input file name")
	exit(0)


if __name__ == "__main__":
	flines = fread(sys.argv[1])

	token_list = ftokenize(flines)
	parse(token_list)
	print_stat()


#

		
#	i=0
#
#	while i < len(flines):
#		line = flines[i]
#		token_list += re.split(' |"|"|,|:|\n', line.replace(" ", "").rstrip())
#		token_list = filter(None, token_list)
#
#		j = 0
#
#		token = token_list[j]
#		if token == '{':
#			
#
#
#		i += 1
#









