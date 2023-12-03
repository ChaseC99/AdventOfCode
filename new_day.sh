#!/bin/bash

# Load the session cookie from the .env file
source ./.env
echo $SESSION

# Get the year
year=$(TZ='America/New_York' date +%Y)

# Get the day
# Default to the current day if no argument is passed
if [ -z "$1" ]
then
    day=$(TZ='America/New_York' date +%d)
else
    day=$1
fi

# Create folder for the day
mkdir $day

# Create the files with some boilerplate code
touch $day/part1.py
printf "file_name = 'demo.txt'\n\nfor line in open(file_name):\n" >> $day/part1.py
touch $day/part2.py

# Create demo and input files. 
touch $day/demo.txt
touch $day/input.txt

# Format the day variable
# For single digit numbers, we need to remove the leading 0
# E.g. 01 -> 1
[[ ${day:0:1} = '0' ]] && formattedDay="${day:1}"

# Fetch the day's input from adventofcode.com
curl -b "session=$SESSION" https://adventofcode.com/$year/day/$formattedDay/input > $day/input.txt
# Remove the newline at the end of the input file
echo -n "$(cat $day/input.txt)" >| "$day/input.txt"