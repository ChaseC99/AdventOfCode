file_name = 'input.txt'

class Packet:
    def __init__(self, raw) -> None:
        self.values = eval(raw)

    def __repr__(self) -> str:
        return str(self.values)
    
    def __str__(self) -> str:
        return self.__repr__()

    def __len__(self):
        return len(self.values)

    def __getitem__(self, i):
        return self.values[i]

    @staticmethod
    def correct_order(left, right):
        return left < right

    @staticmethod
    def compare(left, right):
        # print(f"Compare {left} vs {right}")
        if isinstance(left, int) and isinstance(right, int):
            if left == right:
                return 0
            
            return 1 if right > left else -1
        
        if isinstance(left, int):
            left = [left]
        if isinstance(right, int):
            right = [right]

        if len(left) == 0 and len(right) == 0:
            return 0
        
        if len(left) == 0:
            return 1
        
        if len(right) == 0:
            return -1

        result = Packet.compare(left[0], right[0])

        if result == 0:
            left.pop(0)
            right.pop(0)
            return Packet.compare(left, right)
        else:
            return result
        

    def __lt__(self, other):
        return not self.__gt__(other)
        
    def __gt__(self, other):
        i = 0
        while i < len(other) and i < len(self):
            cmp = Packet.compare(self[i], other[i])
            if cmp == 0:
                i += 1
            elif cmp == 1:
                return False
            elif cmp == -1:
                return True
        
        return len(self) > len(other)

pairs = [[]]
for line in open(file_name):
    if line.strip() == "":
        pairs.append([])
    else:
        pairs[-1].append(Packet(line.strip()))

correct_indices = []
for i in range(len(pairs)):
    l, r = pairs[i]
    if l < r:
        correct_indices.append(i+1)
print(correct_indices)
print(sum(correct_indices))

### TESTS ###
orderTests = [
    ("[1,1,3,1,1] vs [1,1,5,1,1]", True),
    ("[[1],[2,3,4]] vs [[1],4]", True),
    ("[9] vs [[8,7,6]]", False),
    ("[[4,4],4,4] vs [[4,4],4,4,4]", True),
    ("[7,7,7,7] vs [7,7,7]", False),
    ("[] vs [3]", True),
    ("[[[]]] vs [[]]", False),
    ("[1,[2,[3,[4,[5,6,7]]]],8,9] vs [1,[2,[3,[4,[5,6,0]]]],8,9]", False)
]

def runTest(test_number):
    test = orderTests[test_number]
    test_str, expected_result = test
    packets = [Packet(raw) for raw in test_str.split(" vs ")]
    result = Packet.correct_order(packets[0], packets[1])
    
    if not result == expected_result:
        print(f"TEST {str(test_number+1)} FAILED: for {test_str}, expected {str(expected_result)} but recieved {str(result)}")
    else:
        print(f"TEST {str(test_number+1)} PASSED")

def runOrderTests():
    for testIndex in range(len(orderTests)):
        runTest(testIndex)
