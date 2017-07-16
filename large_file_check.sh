find . | xargs ls -al | awk '$5 > 104857600 {print $9}' | grep trace
