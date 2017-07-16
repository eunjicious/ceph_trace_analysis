
bench="swift_4K4K swift_1M1M rados_4K4K rados_4K1M rados_1M1M fio_4K4K fio_1M1M"
bench=`cat _trace_list`

for b in $bench; do
	./3_op_cnt_plot.py all_op_cnt $b
done 
