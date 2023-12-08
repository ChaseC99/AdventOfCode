#!/bin/bash

# NEW DAY SCRIPT
# This script will get you all setup to start solving the challenges for the day.
#
# It creates a new folder with 4 files:
# - demo.txt
#       Empty. Copy/paste from the day's instructions.
# - part1.py
#       Boilerplate code to open demo.py and parse the lines.
# - part2.py
#       Empty. Continue building off of part1.py once completed.
# - input.txt
#       The challenge's input file, loaded from the Advent of Code website.
#
# Usage
# To run the script for the current day:
#   make
#
# To run the script for a specific day, e.g. day 2
# (Include a leading 0 for single digit numbers):
#   make day=02

# Load the session cookie from the .env file
source ./.env

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

# Format the day variable
# For single digit numbers, we need to remove the leading 0
# E.g. 01 -> 1
[[ ${day:0:1} = '0' ]] && formattedDay="${day:1}"

# Generate the url for the day
url="https://adventofcode.com/$year/day/$formattedDay"

# Start message
echo -e "\nCreating \"Advent of Code\" $year Day $day...\n\n"

# Create folder for the day
mkdir $day

# Create the files with some boilerplate code
touch $day/part1.py
printf "# $url\n\nfile_name = 'demo.txt'\n\nfor line in open(file_name):\n\tline = line.strip()" >> $day/part1.py
touch $day/part2.py

# Create demo and input files. 
touch $day/demo.txt
touch $day/input.txt

# Fetch the day's input from adventofcode.com
curl -b "session=$SESSION" $url/input > $day/input.txt
# Remove the newline at the end of the input file
echo -n "$(cat $day/input.txt)" >| "$day/input.txt"

# Open the day's instructions in the browser
open $url

# Open the input file in VS Code
code $day/part1.py

# Goodbye message
echo -e "\n\nAll Done! Happy Coding 🎄"