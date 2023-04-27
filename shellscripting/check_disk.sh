#!/bin/bash
df -H | awk '{print $5 " " $1}' | while read output;
do
	echo "Disk detail : $output"
	usage=$(echo $output | awk '{print $1}' | cut -d'%' -f1)
	echo $usage
done
#awk reads input files line by line and performs 
#actions based on patterns and rules defined by the user.

