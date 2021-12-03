mkdir $1;
touch $1/input.txt;
touch $1/part1.py
echo "file_name = 'input.txt'\n\nfor line in open(file_name):\n" >> $1/part1.py