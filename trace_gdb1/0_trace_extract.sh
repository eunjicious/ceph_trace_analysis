
bench="swift_4K4K swift_1M1M rados_4K4K rados_4K1M rados_1M1M fio_4K4K fio_1M1M"

objstore="ms"
for b in $bench; do
  for os in $objstore; do
    echo $b ...
    log="$b"_"$os".log
    out="$b"_"$os".trc
   # tline=`wc -l rados_trace.log | awk '{print $1}'`
    sline=`grep -n EUNJI $log | grep "start" | awk -F: '{print $1}'`
    eline=`grep -n EUNJI $log | grep "end" | awk -F: '{print $1}'`

    echo "$sline $eline"

    head -n $eline $log > tmp.log
    tail -n $((eline - sline)) tmp.log | grep " 10 " >  $out 
  done
done

rm tmp.log
