
#### dir 


bench="swift_4K4K swift_1M1M rados_4K4K rados_4K1M rados_1M1M fio_4K4K fio_1M1M"
bench="$1"
bench="ycsba_mds ycsbb_mds ycsbc_mds ycsbd_mds ycsbe_mds ycsbf_mds ycsba_fds ycsbb_fds ycsbc_fds ycsbd_fds ycsbe_fds ycsbf_fds"
bench=`cat _trace_list`


for b in $bench; do
	echo $b ...
   log="$b".log
   out="$b".dump
   # tline=`wc -l rados_trace.log | awk '{print $1}'`
   sline=`grep -n "dump" $log | awk -F: '{print $1}'`
   eline=`grep -n  "^}" $log | awk -F: '{print $1}'`

   echo "$sline $eline"

   head -n $eline $log > tmp.log
   tail -n $((eline - sline)) tmp.log >  $out 

	rm tmp.log
done

