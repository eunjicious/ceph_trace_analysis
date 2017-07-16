bench="swift_4K4K swift_1M1M rados_4K4K rados_4K1M rados_1M1M fio_4K4K fio_1M1M"

#### generate data for dist 

if [[ $# -lt 1 ]]; then
	echo "Usage: .sh read write"
	exit
fi

if [[ $1 == "read" ]]; then
	op_list=`cat rop_list`
	echo "read ..."
else
	echo "write ..."
	exit
fi

for b in $bench; do
	i=0
	flist="`echo '-'``echo e` `echo "gtitle='$b'"`"
	if [[ $1 == "read" ]]; then
		output="$b"_r.eps
	else
		output="$b"_w.eps
	fi
	for op in $op_list; do	
		i=$((i+1))
		f=$b.$op

		flist="$flist `echo '-'``echo e` `echo f"$op"=\'$f\'`"
		flist="$flist `echo '-'``echo e` `echo "oname='$output'"`"
	done

	echo $flist
	gnuplot $flist 5_gnuplot_rsize_plot.cfg
	open "$output"
done



