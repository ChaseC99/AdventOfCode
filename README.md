# Advent of Code 🎄
[Advent of Code](https://adventofcode.com) is one of my favorite holiday traditions! 
Each day a new 2-part coding challenge is released for everyone to solve.

| | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |
| -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
|2022|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|||||||||||||||||
|2021|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️||⭐️|⭐️⭐️|||||||||||||||
|2020|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|||||||||| 

## New Day Script
This script will get you all setup to start solving the challenges for the day.

It creates a new folder with 4 files: `demo.txt`, `part1.py`, `part2.py`, `input.txt`.   
`part1.py` has some boilerplate code to open `demo.py` and parse the lines.  
`input.txt` has the challenge's input file, loaded from the Advent of Code website.  

Call the script with the day as an arg. _Add a leading 0 for single digit numbers._  
Example: `./new_day.sh 01`

## Getting Setup
- Clone the repository  
`git clone git@github.com:ChaseC99/AdventOfCode.git`
- Create a new branch for the year  
`git checkout -b YEAR`
- Delete the files for the previous year
- Create the .env file  
`cp .env.sample .env`
- Navigate to [Advent of Code](https://adventofcode.com/), get the value of your `session` cookie, and add it to the `.env` file
