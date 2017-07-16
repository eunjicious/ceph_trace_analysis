

if [[ $# -lt 1 ]]; then
	echo "Usage: .sh read write"
	exit
fi

if [[ $1 == "read" ]]; then
	op_list=`cat rop_list`
else
	op_list=`cat wop_list`
fi


bench="swift_4K4K swift_1M1M rados_4K4K rados_4K1M rados_1M1M fio_4K4K fio_1M1M"
for b in $bench; do

	trc_file="$b".trc
	echo $trc_file ...
	grep "~" $trc_file | awk -F'~' '{print $1, $2}' | awk '{print $6, $NF}' > tmp.file

#	awk '$1=="_omap_setkeys" {print $1}' tmp.file
#	cat tmp.file
	for op in $oplist; do
		echo $op
#		awk '$1 == "$op" {print $1, $2}' tmp.file | sort | uniq -c  
		awk  '$1 =="'"$op"'" {print $1, $2 }' tmp.file | sort | uniq -c > $b.$op
		#awk '$1 == "_omap_setkeys" {print '"${op}"'$1, $2}' tmp.file | sort | uniq -c  
	done
done


