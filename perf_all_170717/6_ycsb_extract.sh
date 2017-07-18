
store="filestore bluestore"
workloads="a b c d e f"

for wo in $workloads; do
	rm tmp.data
	touch tmp.data

	for st in $store; do
		cd $st
		grep "Average" ycsb$wo.perf \
		| sed 's/:/ /g' | sed 's/\[/ /g' | sed 's/\]/ /g' \
		| awk '{print $1, $4}' | awk '{print $1, "'"$st"'", $0}' >> ../tmp.data
#		| sort
#		| sort | awk '{print $2, "'"ycsb$wo"'", $3, $4}' >> ../tmp.data 
		cd ..
	done
	#sort tmp.data > ycsb$w.data
	echo "# line store wor latency" > ycsb$wo.data
	sort -r tmp.data | awk 'BEGIN {line= 0} { line +=1; if (line%3 == 0) {print line, 0, 0, 0; line += 1;} printf("%d %s %s %d\n", line, $2, $3, $4);}' >> ycsb$wo.data
	cat ycsb$wo.data
	echo
done

#echo "# line store wor iops" > rados-all.data
#awk 'BEGIN {line = 0} { line +=1; if (line%3 == 0) {print line, 0, 0, 0; line +=1} print line, $0}' tmp.data >> rados-all.data
#
#cat rados-all.data
#
