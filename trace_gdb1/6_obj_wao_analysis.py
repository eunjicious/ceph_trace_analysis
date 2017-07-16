#! /usr/bin/python2.7

import sys
from subprocess import call

#bench = ["swift", "rados", "fio"]
bench=["swift_4K4K", "swift_1M1M", "rados_4K4K", "rados_4K1M", "rados_1M1M", "fio_4K4K", "fio_1M1M"]
wop=["_write", "_setattrs", "_omap_setheader", "_omap_setkeys"]

op_tbl = {'key':[0, 0, 0, 0, 0, 0, 0]}

obj_tbl = {'obj' : [0, 0, 0, 0]}

### file read 
lines = ["" for i in range(len(bench))]

for i in range(len(bench)):

	ofname = bench[i] + ".obj_cnt_all"

	for j in range(len(wop)):
		op =wop[j] 
		ifname = bench[i] + ".obj_cnt." + op
		print ifname
		opfile = open(ifname, "r")
		oplines = opfile.readlines()

		for opline in oplines:
			token = opline.rstrip().split(' ')
			obj = token[0]
			cnt = token[1]

			if obj in obj_tbl.keys():
				obj_tbl[obj][j] = j+1
#				count = obj_tbl[obj]
#				count[j] += long(cnt)  
			else:
				count = [0, 0, 0, 0]
#				count[j] += long(cnt)  
				count[j] = j+1
				obj_tbl[obj] = count
	### oplist file read 
	objfname = bench[i] + ".obj_list"
	with open(objfname) as objfile:
		objlist = objfile.readlines() 
	objfile.close

	## write 
	outfile = open(ofname, "w")
	for obj in objlist:
		k = obj.rstrip()
		if not k in obj_tbl.keys():
			print("not found: " + k)
#		print (k, obj_tbl[k])	
		oline = k + " " + ' '.join(map(str, obj_tbl[k])) + '\n'
		outfile.write (oline)
#

#	call(["cat", ofname])


"""

  ifname = bench[i] + ".obj_cnt"

  with open(ifname) as fo:
    lines[i] = fo.readlines()

  fo.close

### fill out table
for i in range(len(bench)):
  for line in lines[i]:
    words = line.rstrip().split(' ')
#    print(words[0], words[1])
    func = words[0]
    if func in op_tbl.keys():
      count = op_tbl[func]
      count[i] += long(words[1])
    else:
      count = [ 0, 0, 0, 0, 0, 0, 0]
      count[i] += long(words[1])
    op_tbl[func] = count



### oplist file read 
opfname = "op_list.reverse"
with open(opfname) as opfile:
	oplist = opfile.readlines() 
opfile.close

## write data file 
ofname="all_op_cnt.data"
outfile = open(ofname, "w")
#print "# func swift rados fio"
#outfile.write( "# func swift rados fio\n")


outfile.write( "# func swift_4K4K swift_1M1M rados_4K4K rados_4K1M rados_1M1M fio_4K4K fio_1M1M\n")

for op in oplist: 
	k = op.rstrip()
	oline = k + " " + ' '.join(map(str, op_tbl[k])) + '\n'
	outfile.write (oline)
#	print(oline);
#
#for k in op_tbl: 
##  print k, ' '.join(map(str, op_tbl[k]))
#  oline = k + " " + ' '.join(map(str, op_tbl[k])) + '\n'
#  outfile.write (oline)
#
print ("output is " + ofname + "...")

outfile.close
"""
