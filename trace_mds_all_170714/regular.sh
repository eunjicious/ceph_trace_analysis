trace=`cat _trace_list`

for trc in $trace; do
	awk '$4 > 0 {print $0}' $trc.prs > "$trc"_reg.prs
done
