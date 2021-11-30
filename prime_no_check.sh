#!/bin/bash
#echo "Please provide a number to check prime number: "
#read n
n=111
count=0

#a=$((10 % 2))
#echo ${a}


for ((i=1; i <= $n; i++))
do
    if [[ ${i} != 1 && ${i} != "${n}" ]]
    then
        remainder=$(($n % $i))
        if [[ ${remainder} = 0 ]]
        then
            count=$((count + 1))
        fi
    fi
done


if [[ ${count} = 0 ]]
then
  echo "Number is prime"
else
  echo "Number is not prime"
fi
