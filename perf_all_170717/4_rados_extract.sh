
size="4k4k 4k1m 1m1m"
store="filestore bluestore"

rm tmp.data
touch tmp.data

for sz in $size; do
	for st in $store; do
		cd $st
		grep "Average IOPS" rados-$sz.perf \
		| sed 's/-/ /g' | sed 's/.perf/ /g'\
		| awk '{print "'"$sz"'", "'"$st"'", $0}'\
		| sort | awk '{print $2, "'"$sz"'", $5}' >> ../tmp.data 
		cd ..
	done

done

echo "# line store wor iops" > rados-write.data
awk 'BEGIN {line = 0} { line +=1; if (line%3 == 0) {print line, 0, 0, 0; line +=1} print line, $0}' tmp.data >> rados-write.data

cat rados-write.data

