#bench="swift_4K4K swift_1M1M rados_4K4K rados_4K1M rados_1M1M fio_4K4K fio_1M1M"
#bench="swift_4K4K"
bench=`cat _trace_list`

#### generate data for dist 


for b in $bench; do
	f=$b.prs
	output=$f.eps
	flist="`echo '-'``echo e` `echo "gtitle='$b'"`"

	flist="$flist `echo '-'``echo e` `echo datafile=\'$f\'`"
	flist="$flist `echo '-'``echo e` `echo "oname='$output'"`"

	gnuplot $flist 2_gnuplot_len.cfg
	open "$output"
done

for b in $bench; do
	f="$b"_reg.prs
	output=$f.eps
	flist="`echo '-'``echo e` `echo "gtitle='$b'"`"

	flist="$flist `echo '-'``echo e` `echo datafile=\'$f\'`"
	flist="$flist `echo '-'``echo e` `echo "oname='$output'"`"

	gnuplot $flist 2_gnuplot_len.cfg
	open "$output"
done



