file_name = 'input.txt'
from collections import defaultdict

class Hand:
    def __init__(self, string) -> None:
        cards, bid = string.split(" ")
        self.cards_str = cards
        self.cards = [self._card_value(card) for card in cards]
        self.of_a_kind = self._count_same_cards(self.cards)
        self.bid = int(bid)
    
    @staticmethod
    def _card_value(card):
        if card == 'T':
            return 10
        elif card == 'J': 
            # Joker
            return 1
        elif card == 'Q':
            return 12
        elif card == 'K':
            return 13
        elif card == 'A':
            return 14
        else:
            return int(card)

    @staticmethod
    def _count_same_cards(cards):
        card_count = defaultdict(int)
        for card in cards:
            card_count[card] += 1
        
        # Remove j from the count
        joker_count = card_count[1]
        del card_count[1]

        sorted_values = sorted(card_count.values(), reverse=True)
        
        # Five of a kind
        if joker_count == 5 or sorted_values[0] + joker_count == 5:
            return 5
        
        # Four of a kind
        if sorted_values[0] + joker_count == 4:
            return 4
        
        # Full house
        if (sorted_values[0] + joker_count == 3 and sorted_values[1] == 2) or (sorted_values[0] == 3 and sorted_values[1] + joker_count == 2):
            return 3.5

        # Three of a kind
        if sorted_values[0] + joker_count == 3:
            return 3
        
        # Two pair
        if sorted_values[0] == 2 and sorted_values[1] + joker_count == 2:
            return 2.5

        # One pair
        if sorted_values[0] + joker_count == 2:
            return 2

        # High card    
        return sorted_values[0] + joker_count

    def __gt__(self, hand):
        if self.of_a_kind == hand.of_a_kind:
            for i in range(5):
                if self.cards[i] != hand.cards[i]:
                    return self.cards[i] > hand.cards[i]
            
            # If we get here, the hands are equal
            return False
        else:
            return self.of_a_kind > hand.of_a_kind

    def __ge__(self, hand):
        return self > hand or self == hand

    def __lt__(self, hand):
        return not self >= hand

    def __le__(self, hand):
        return not self > hand

    def __eq__(self, hand):
        if self.of_a_kind == hand.of_a_kind:
            for i in range(5):
                if self.cards[i] != hand.cards[i]:
                    return False
            
            # If we get here, the hands are equal
            return True
        
        return False

    def __str__(self) -> str:
        return f"{self.cards_str} {self.bid}"

    def __repr__(self) -> str:
        return self.__str__()
    

hands = []
for line in open(file_name):
    hands.append(Hand(line.strip()))

sorted_hands = sorted(hands, reverse=True)
print(sorted_hands)

total_winnings = 0
num_hands = len(sorted_hands)
for i in range(num_hands):
    total_winnings += sorted_hands[i].bid * (num_hands - i)

print(total_winnings)