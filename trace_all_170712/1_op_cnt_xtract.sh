#bench="swift_4K4K swift_1M1M rados_4K4K rados_4K1M rados_1M1M fio_4K4K fio_1M1M"
#bench="ycsba_mds ycsbb_mds ycsbc_mds ycsbd_mds ycsbe_mds ycsbf_mds ycsba_fds ycsbb_fds ycsbc_fds ycsbd_fds ycsbe_fds ycsbf_fds"
bench=`cat _trace_list`

for b in $bench; do
	dir="$b"
  	f="$dir/$b".trc
  	output="$dir/$b".opcnt
  	echo $f ... 
  	awk '{print $6}' $f | grep -v "statfs:" | grep -v "get_omap_iterator" | sort | uniq -c | awk '{print $2, $1}' | sort > $output

	cat $output
	echo " "
done
