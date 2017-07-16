
trace=`cat _trace_list`

for trc in $trace; do
	f=$trc.prs
	awk '{print $7, $0}' $f | sort -rn | awk '{print $4 $1}' | awk -F":" '{printf(":%s:\n", $3)}'> $trc.obj_sorted
done
