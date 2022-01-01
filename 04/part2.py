file_name = 'input.txt'

class Card:
    def __init__(self, rows) -> None:
        self.rows = rows
        
        self.num_dict = dict()
        r = 0
        for row in rows:
            c = 0
            for val in row:
                self.num_dict[val] = [r,c]
                c += 1
            r += 1

        self.rows_count = [0]*5
        self.cols_count = [0]*5

    def __repr__(self) -> str:
        to_str = '\n'
        for row in self.rows:
            to_str += "\t".join(row) + "\n"
        return to_str

    def __eq__(self, __o: object) -> bool:
        return __o.rows == self.rows

    def _get_row(self, row_number):
        return self.rows[row_number]

    def _get_col(self, col_number):
        col = []
        for row in self.rows:
            col.append(row[col_number])
        return col

    def has_bingo(self, number):
        if not number in self.num_dict:
            return False
        
        row, col = self.num_dict[number]
        del(self.num_dict[number])

        self.rows_count[row] += 1
        if self.rows_count[row] == 5: return self._get_row(row)

        self.cols_count[col] += 1
        if self.cols_count[col] == 5: return self._get_col(col)

    def unmarked_sum(self):
        return sum([int(num) for num in self.num_dict.keys()])

lines = open(file_name).readlines()

bingo_nums = lines[0].strip().split(',')

cards = []
curr_card = []
for line in lines[1:]:
    if line.strip() == '':
        if len(curr_card) > 1:
            cards.append(Card(curr_card))
            curr_card = []
    else:
        curr_card.append([val for val in line.strip().split(' ') if val != ''])
cards.append(Card(curr_card))

for num in bingo_nums:
    cards = [card for card in cards if not card.has_bingo(num)]
    if len(cards) == 1:
        last_card = cards[0]
    if len(cards) == 0:
        unmarked_sum = last_card.unmarked_sum()
        print(f'{unmarked_sum} * {num} = {unmarked_sum * int(num)}')
        quit()
