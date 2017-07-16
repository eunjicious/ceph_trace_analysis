
trace=`cat _trace_list`

for trc in $trace; do
	echo "$trc ..."
	rm $trc.obj_stat
	touch $trc.obj_stat
	obj_list=`cat $trc.obj_sorted`	
	for obj in $obj_list; do
		grep -rn $obj $trc.log | awk -F"~" '{ s += $2} END {print "'"$obj"'",s/NR, NR}' >> $trc.obj_stat
	done
done
