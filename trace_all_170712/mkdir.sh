bench="ycsb"
workload="a b c d e f"
conf="mds fds"

for w in $workload; do
	for c in $conf; do
		dname="$bench$w"_"$c"	
		echo $dname
		if ! [ -d $dname ]; then
			mkdir $dname
		fi
		mv $dname.log $dname
	done
done
