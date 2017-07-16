trace=`cat _trace_list`


echo "data min max avg" > data.min_max_avg
for trc in $trace;do
	awk 'BEGIN{ dmin = 10000}{
		if ( $4 > 0 && dmin > $4) dmin = $4; 
		if (dmax < $4) dmax = $4;
		dsum += $4;
	} END {
		printf("%s %ld %ld %ld\n", "'"$trc"'", dmin, dmax, dsum/NR)
	}' "$trc".prs >> data.min_max_avg
done


echo "xattr min max avg" > xattr.min_max_avg
for trc in $trace;do
	awk 'BEGIN{ dmin = 10000}{
		if ( $5 > 0 && dmin > $5) dmin = $5; 
		if (dmax < $5) dmax = $5;
		dsum += $5;
	} END {
		printf("%s %ld %ld %ld\n", "'"$trc"'", dmin, dmax, dsum/NR)
	}' "$trc".prs >> xattr.min_max_avg
done

echo "omap_header min max avg" > omap_header.min_max_avg
for trc in $trace;do
	awk 'BEGIN{ dmin = 10000}{
		if ( $6 > 0 && dmin > $6) dmin = $6; 
		if (dmax < $6) dmax = $6;
		dsum += $6;
	} END {
		printf("%s %ld %ld %ld\n", "'"$trc"'", dmin, dmax, dsum/NR)
	}' "$trc".prs >> omap_header.min_max_avg
done


echo "omap min max avg" > omap.min_max_avg
for trc in $trace;do
	awk 'BEGIN{ dmin = 10000}{
		if ( $7 > 0 && dmin > $7) dmin = $7; 
		if (dmax < $7) dmax = $7;
		dsum += $7;
	} END {
		printf("%s %ld %ld %ld\n", "'"$trc"'", dmin, dmax, dsum/NR)
	}' "$trc".prs >> omap.min_max_avg
done
