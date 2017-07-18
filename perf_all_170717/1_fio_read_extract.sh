
size="4k 1m"
store="filestore bluestore"


for sz in $size; do
	rm tmp.data
	touch tmp.data

	for st in $store; do
		cd $st
		grep "iops" fio*-$sz.perf | grep read \
		| sed "s/-read-/-seqrd-/g"\
		| sed "s/-rw-/-seqmix-/g"\
		| sed "s/-randread-/-randrd-/g" \
		| sed "s/-randrw-/-randmix-/g"\
		| awk -F"=" '{print $1, $2, $3, $4, $5}' \
		| sed 's/KB,//g' | sed 's/KB\/s,//g' | sed 's/, / /g' \
		| sed 's/msec//g' | sed 's/\.perf://g' | sed 's/fio-//g' \
		| sed "s/-$sz//g" | sed "s/MB//g"\
		| sed "s/read :/read:/g"\
		| awk '{print $1, "'"$st"'", "'"$sz"'", $1, $4, $6, $8, $10}' >> ../tmp.data 
		#| awk '{print $1, "'"$st"'", "'"$sz"'", $1, $4, $6, $8}' >> ../tmp.data
		cd ..
	done
	cat tmp.data
	sort -r tmp.data | awk 'BEGIN {line= 0} { line +=1; if (line%3 == 0) {print line, 0, 0, 0, 0, 0, 0, 0; line += 1;} print line, $2, $3, $4, $5, $6, $7, $8;}' > tt

	echo "# line store size wor io bw iops runt"> fio_read_$sz.data
	cat tt >> fio_read_$sz.data
	cat fio_read_$sz.data

#	echo "what" >> fio_read_$sz.data
#	cat ttt >> fio_read_$sz.data 
#	cat fio_all_$sz.data
	echo 
done

