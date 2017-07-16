
bench="swift_4K4K swift_1M1M rados_4K4K rados_4K1M rados_1M1M fio_4K4K fio_1M1M"

for b in $bench; do
  f="$b".trc
  output="$b"_ms.opcnt
  echo $f ... 
  awk '{print $6}' $f | grep -v "statfs:" | grep -v "get_omap_iterator" | sort | uniq -c | awk '{print $2, $1}' | sort > $output
done
