#!/bin/bash

# Load the session cookie from the .env file
source ./.env
echo $SESSION

# Name the day paramater
day=$1

# Create folder for the day
mkdir $day

# Create the files with some boilerplate code
touch $day/part1.py
printf "file_name = 'input.txt'\n\nfor line in open(file_name):\n" >> $day/part1.py
touch $day/part2.py

# Create demo and input files. 
touch $day/demo.txt
touch $day/input.txt

# Format the day variable
# For single digit numbers, we need to remove the leading 0
# E.g. 01 -> 1
[[ ${day:0:1} = '0' ]] && day="${day:1}"

# Fetch the day's input from adventofcode.com
curl -b "session=$SESSION" https://adventofcode.com/2021/day/$day/input > $1/input.txt
# Remove the newline at the end of the input file
echo -n "$(cat $1/input.txt)" >| "$1/input.txt"