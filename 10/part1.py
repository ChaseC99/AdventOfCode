file_name = 'input.txt'

x = 1
cycle = 0
signals = 0

def increment_cycle():
    global x, cycle, signals
    cycle += 1

    if cycle == 20 or (cycle-20) % 40 == 0:
        signal_strength = x*cycle
        signals += signal_strength
        print(f"Cycle {cycle}: X={x}, Signal Strength={signal_strength}")

for line in open(file_name):
    line = line.strip()
    if line.startswith("noop"):
        increment_cycle()
    if line.startswith("addx"):
        val = int(line.split()[1])
        increment_cycle()
        increment_cycle()
        x += val

print(signals)