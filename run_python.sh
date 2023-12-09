#!/bin/bash

# RUN PYTHON SCRIPT
# This script runs the python script for the current day.

# Get the day
# Default to the current day if no argument is passed
if [ -z "$1" ]
then
    day=$(TZ='America/New_York' date +%d)
else
    day=$1
fi

# Navigate to the directory of this script
cd $day

# Check if part2.py is empty
if [ ! -s "part2.py" ]
then
    # Part 2 not started yet
    # Run part1.py
    python3 part1.py
else
    # Part 2 has been started
    # Run part 2
    python3 part2.py
fi