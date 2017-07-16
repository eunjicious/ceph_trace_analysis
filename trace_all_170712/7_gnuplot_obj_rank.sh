bench="swift_4K4K swift_1M1M rados_4K4K rados_4K1M rados_1M1M fio_4K4K fio_1M1M"
bench=`cat _trace_list`

#### generate data for dist 

op_list=`cat wop_list`

for b in $bench; do
	i=0
	flist="`echo '-'``echo e` `echo "gtitle='$b'"`"

	for op in $op_list; do	

		if [[ $op == "_omap_setheader" ]]; then
			continue
		fi

		i=$((i+1))
		f=$b/$b.obj_cnt.$op
		output=$f.eps

		flist="$flist `echo '-'``echo e` `echo datafile=\'$f\'`"
		flist="$flist `echo '-'``echo e` `echo "oname='$output'"`"
		flist="$flist `echo '-'``echo e` `echo "gtitle='$f'"`"

		echo $flist
		gnuplot $flist 7_gnuplot_obj_rank.cfg
		open "$output"

	done
done



