#
#if [[ $# -lt 1 ]]; then
#	echo "Usage: .sh [`cat wop_list`]"
#	exit
#fi
#
#
#op=$1
bench="swift_4K4K swift_1M1M rados_4K4K rados_4K1M rados_1M1M fio_4K4K fio_1M1M"
bench=`cat _trace_list`
oplist="_write _setattrs _omap_setkeys _omap_setheader"
#oplist="_omap_setheader _omap_setkeys _setattrs _write"

for b in $bench; do
	for op in $oplist; do
		infile="$b/$b".trc

		#### count object access for operations 
		ofile="$b/$b".obj_cnt.$op
		echo $infile ...
		grep $op $infile | awk -F: '{print $4}' | sort | uniq -c | sort -nr | awk '{print $2, $1}' > $ofile


		#### uniq object list for operations 
		ofile="$b/$b".obj.$op
		grep $op $infile | awk -F: '{print $4}' | sort | uniq  > $ofile 

#
#		#### make uniq object list sorted in operations  
#		infile=$ofile	
#		ofile="$b/$b".obj_list
#		echo "$ofile .... start "
#		rm $ofile
#		touch $ofile
#		rm objlist.tmp 
#
#		new_obj_list=`cat $infile`
#
#		for obj in $new_obj_list; do
#			if ! grep -Fxq $obj $ofile
#			then
#				echo "add $obj"
#				echo $obj >> $ofile				
#			fi
#		done
#	  
#		echo "$ofile .... end "
#		wc -l $ofile
#	  
#		
#		### test
#		cat $infile
#		cat $infile >> objlist.tmp
#
	done
done


for b in $bench; do
	ofile="$b/$b".obj_list
	rm $ofile
	touch $ofile
	rm objlist.tmp

	for op in $oplist; do
		infile="$b/$b".obj.$op	
		echo $infile ... 

		new_obj_list=`cat $infile`

		for obj in $new_obj_list; do
			if ! grep -Fxq $obj $ofile
			then
				echo $obj >> $ofile				
			fi

#			case $obj in 
#				$curr_obj_list) ;;
#				*) echo $obj >> $ofile;;
#			esac
		done
		
		### test
		cat $infile >> objlist.tmp
		

#		grep $op $infile | awk -F: '{print $1}' | sort | uniq >> $ofile
	done
	sort objlist.tmp | uniq | wc -l 
	wc -l $ofile
done


