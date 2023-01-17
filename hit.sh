#!/bin/bash

file = Outputhits.txt

clear
if [ -f $file ];then
        rm -rf Outputhits.txt
fi

read -p "Put a word to check: " word
echo ""
read -p "Please put the IP from the container VM: " ip
echo ""
read -p "How many time do you want to hit the API? " hit


x=1
while [ $x -le $hit ]   
        do
                curl $ip/palindrome/$word >> Outputhits.txt
                echo " " >> Outputhits.txt
                echo " " >> Outputhits.txt
                let x+=1
        done
echo " " 
cat Outputhits.txt
sleep 8
clear
