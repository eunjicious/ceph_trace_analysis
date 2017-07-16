#! /usr/bin/python2.7

from subprocess import call
#bench=["ycsba_mds", "ycsbb_mds", "ycsbc_mds", "ycsbd_mds", "ycsbe_mds", "ycsbf_mds"] 

#### read trace list 
bench_fname="_trace_list"
bench_fo = open(bench_fname, "r")
bench_raw = bench_fo.readlines()

bench=[]
for trc in bench_raw:
	bench.append(trc.strip())

#print(bench)
	

### oplist file read 
op_list_fname = "op_list.reverse"
op_list_fo = open(op_list_fname)
oplist = op_list_fo.readlines() 
op_list_fo.close

#### initialize op_tbl 
count=[0 for i in range(len(bench))]
op_tbl = {'key' : count }

for op in oplist:
  count=[0 for i in range(len(bench))]
  op_tbl[op.rstrip()] = count

### file read 
lines = ["" for i in range(len(bench))]

for i in range(len(bench)):
  ifname = bench[i] + "/" + bench[i] + ".opcnt"
  print (ifname)

  with open(ifname) as fo:
	lines[i] = fo.readlines()

  fo.close

### fill out table
for i in range(len(bench)):
  ## for each trace
  print(bench[i])
  for line in lines[i]:
	words = line.rstrip().split(' ')
	op = words[0]
	op_tbl[op][i] = op_tbl[op][i] + long(words[1])

## write data file 
out_fname="all_op_cnt.data"

out_fo = open(out_fname, "w")

first_line = "# func"
for b in bench:
  first_line = first_line + " " + b
first_line = first_line + "\n"

#print(first_line)
out_fo.write(first_line)
#out_fo.write( "# func swift_4K4K swift_1M1M rados_4K4K rados_4K1M rados_1M1M fio_4K4K fio_1M1M\n")
#out_fo.write("# func ycsba_mds ycsbb_mds ycsbc_mds ycsbd_mds ycsbe_mds ycsbf_mds\n") 

for op in oplist: 
  k = op.rstrip()
  oline = k + " " + ' '.join(map(str, op_tbl[k])) + '\n'
  out_fo.write (oline)

print ("output is " + out_fname + "...")


out_fo.close

### print results 
#call(["cat", out_fname]) ### not working 

