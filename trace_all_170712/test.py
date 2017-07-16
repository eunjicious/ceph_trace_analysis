#! /usr/bin/python2.7


tlist_fname="_trace_list"
tlist_fo = open(tlist_fname, "r")
tlist_raw = tlist_fo.readlines()

tlist=[]
for trc in tlist_raw:
	tlist.append(trc.strip())

print(tlist)
	
####

count=[0 for i in range(len(tlist))]
#for i in range(len(tlist)):
#	count.append(0)

print(count) 

####
op_tbl = {'key':count}
op_tbl["_write"] = count
op_tbl["_setattr"] = count

print (op_tbl["_write"][0])

op_tbl["_write"][0] += 10
print (op_tbl)

#
#ofname="all_op_cnt.data"
#from subprocess import call
#call(["cat", ofname])
##
