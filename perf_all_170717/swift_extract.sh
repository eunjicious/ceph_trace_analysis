
workloads=`grep FINAL filestore/*.perf | awk '{print $6}' | sort | uniq`
store="filestore bluestore"
size="1m 4k"


rm tmp.data
touch tmp.data
for st in $store; do
	cd $st 
	for sz in $size; do
		avg=""
		f=swift-$sz.perf
		for wor in $workloads; do
			grep $wor $f | sed 's/\/s//g' | awk '{s+=$10} END {print "'"$sz"'","'"$wor"'",  "'"$st"'", s/NR}' >> ../tmp.data
		done
		#echo $sz $st $avg >> ../tmp.data
	done
	cd ..
done

echo "# line size wor store iops"> swift_all.data
sort tmp.data | awk 'BEGIN {line= 0} { line +=1; if (line%3 == 0) {print line, 0, 0, 0, 0, 0; line += 1;} print line, $1, $2, $3, $4, $5;}' >> swift_all.data

cat swift_all.data
