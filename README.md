# Advent of Code 🎄
[Advent of Code](https://adventofcode.com) is one of my favorite holiday traditions! 
Each day a new 2-part coding challenge is released for everyone to solve.

| | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |
| -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
|2023|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️|⭐️⭐️|⭐️⭐️||||||||||||||||||
|2022|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️|⭐️⭐️|||⭐️⭐️||||||||||||
|2021|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️||⭐️|⭐️⭐️|||||||||||||||
|2020|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|⭐️⭐️|||||||||| 

## New Day Script
This script will get you all setup to start solving the challenges for the day.

It creates a new folder with 4 files: 
- `demo.txt`  
Empty. Copy/paste from the day's instructions.
- `part1.py`  
Boilerplate code to open `demo.py` and parse the lines.
- `part2.py`  
Empty. Continue building off of `part1.py` once completed.
- `input.txt`  
The challenge's input file, loaded from the Advent of Code website.  

### Usage
To run the script for the current day:
```bash
make
```

To run the script for a specific day, e.g. day 2  
(_Include a leading 0 for single digit numbers_):
```bash
make day=02
```

## Getting Setup
- Clone the repository  
`git clone git@github.com:ChaseC99/AdventOfCode.git`
- Create a new branch for the year  
`git checkout -b YEAR`
- Delete the files for the previous year
- Create the .env file  
`cp .env.sample .env`
- Navigate to [Advent of Code](https://adventofcode.com/), get the value of your `session` cookie, and add it to the `.env` file
