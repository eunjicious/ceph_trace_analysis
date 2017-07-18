#/bin/bashh


extract () {
	
	echo "======= 1. extract ====="
	buff="256 512 1024 2048"
	
	for b in $buff; do
		th=1
		while [ $th -le 4 ]; do
			fname=`echo $th`_fio_b$b
			tfname=$fname.txt
			echo $fname
	
			grep -rn "th=\[" $tfname | awk -F"th=" '{print $2, $3, $4, $5}' | sed 's/,//g' | sed 's/\[//g' | sed 's/\]//g' | awk '{print $1, $3, $5, $7}' | tr ' ' '\n' > $fname.resp
	
			th=$((th+1))
		done
	done
}

############# merge 

merge() {
	echo "======= 2. merge ====="
	opt=$1
	tmpfname=tmp.resp

	buff=(256 512 1024 2048)
	fval=()

	echo "1 5 10 20 30 40 50 60 70 80 90 95 99 99.5 99.9 99.95 99.99" > $tmpfname
	percentile=(1 5 10 20 30 40 50 60 70 80 90 95 99 99.5 99.9 99.95 99.99)
	#echo $percentile 
	col=${#percentile[@]}
	echo $col

	th=0
	while [ $th -lt 4 ]; do
		### read 
		b=0
		while [ $b -lt 4 ]; do
			fname=`echo $((th+1))`_fio_b${buff[$b]}.resp
			echo $fname
			fval[$b]=$(<$fname)
#			echo `echo $((th+1))`_`echo ${buff[$b]}`_`echo $opt` ${fval[$b]} >> $tmpfname
			echo ${fval[$b]} >> $tmpfname
			b=$((b+1))
		done	
	
		th=$((th+1))
	done

	c=1
	row=0
	ffname=fio_all_$opt.resp

	rm $ffname
#	echo > $ffname
	while [ $c -le 17 ]; do
		exec < $tmpfname
		while read line; do
			row=$((row+1))
			echo $line > tt
			awk '{print $'"$c"'}' tt | tr '\n' ' ' >> $ffname
		done
		echo "" >> $ffname
		c=$((c+1))
	done

	mv $ffname ..
}


opt="flush noflush rflush"

for o in $opt; do
	echo $o
	cd $o
	find . -name "*_fsy_*" | sed -e 'p' -e 's/fsy/fio/g' | xargs -n 2 mv
	extract
	merge $o
	cd ..
done	
