#!/bin/bash

if [ -f Outputhits.txt ];then
	rm -rf Outputhits.txt
fi
	
read -p "Put a word: " word
read -p "How many time do you want to hit the API? " hit


x=1
while [ $x -le $hit ]	
	do 
		curl localhost:8181/palindrome/$word >> Outputhits.txt
		echo " " >> Outputhits.txt
		echo " " >> Outputhits.txt
		let x+=1 
	done
