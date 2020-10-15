#!/bin/bash

# TODO: find an apropriate name cheme to execute python, use the input and compare to expected values

for i in $(ls $1-input-*.txt); do 
	cat $i | python $(ls $1-*.py)
	#echo expecting:
	#echo expect.$i
	echo
done
