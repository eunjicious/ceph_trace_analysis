bench="swift_4K4K swift_1M1M rados_4K4K rados_4K1M rados_1M1M fio_4K4K fio_1M1M"
#bench="swift_4K4K"

#### generate data for dist 

op_list=`cat wop_list`

for b in $bench; do
	i=0
	f=$b.obj_cnt_all
	output=$f.eps
	flist="`echo '-'``echo e` `echo "gtitle='$b'"`"

	flist="$flist `echo '-'``echo e` `echo datafile=\'$f\'`"
	flist="$flist `echo '-'``echo e` `echo "oname='$output'"`"

	gnuplot $flist 6_gnuplot_obj.cfg
	open "$output"

done



