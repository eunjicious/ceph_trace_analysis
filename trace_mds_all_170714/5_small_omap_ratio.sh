
trace=`cat _trace_list`

for trc in $trace; do
	awk '{ if ($7 > 0){
			tot ++; 
			if ($7 < 4096)
				c ++;
			}
		} END { printf("%s %.2f\n", "'"$trc"'", c/tot)}' $trc.prs
done
