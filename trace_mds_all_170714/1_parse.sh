
bench=`cat _trace_list`

for b in $bench; do
	echo "./1_parse.py $b.dump"
	./1_parse.py $b.dump > $b.prs
	wc -l $b.prs
done
