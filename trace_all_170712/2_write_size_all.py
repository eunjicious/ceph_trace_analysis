#! /usr/bin/python2.7


bench = ["swift", "rados", "fio"]

op_tbl = {'key':[0, 0, 0]}


### file read 
lines = ["" for i in range(len(bench))]

for i in range(len(bench)):
  ifname = bench[i] + "/" + bench[i] + ".opcnt"

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
      count[i] += int(words[1])
    else:
      count = [ 0, 0, 0]
      count[i] += int(words[1])
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
outfile.write( "# func swift rados fio\n")


for op in oplist: 
	k = op.rstrip()
	oline = k + " " + ' '.join(map(str, op_tbl[k])) + '\n'
	outfile.write (oline)
	print(oline);
#
#for k in op_tbl: 
##  print k, ' '.join(map(str, op_tbl[k]))
#  oline = k + " " + ' '.join(map(str, op_tbl[k])) + '\n'
#  outfile.write (oline)
#
print ("output is " + ofname + "...")

outfile.close
