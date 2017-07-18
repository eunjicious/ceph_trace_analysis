
store="filestore bluestore"
workloads="seqr randr"

rm tmp.data
touch tmp.data

for wor in $workloads; do
	for st in $store; do
		cd $st
		grep "Average IOPS" rados-$wor.perf \
		| sed 's/-/ /g' | sed 's/.perf/ /g'\
		| awk '{print "'"$wor"'", "'"$st"'", $0}'\
		| sort | awk '{print $2, "'"$wor"'", $5}' >> ../tmp.data 
		cd ..
	done

done

echo "# line store wor iops" > rados-read.data
awk 'BEGIN {line = 0} { line +=1; if (line%3 == 0) {print line, 0, 0, 0; line +=1} print line, $0}' tmp.data >> rados-read.data

cat rados-read.data

