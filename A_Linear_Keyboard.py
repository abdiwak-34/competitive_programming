def calculate_typing_time(keyboard, word):
    position_map = {char: idx for idx, char in enumerate(keyboard)}
    total_time = 0
    for i in range(1, len(word)):
        total_time += abs(position_map[word[i]] - position_map[word[i-1]])
    
    return total_time
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
results = []
for i in range(t):
    keyboard = data[2 * i + 1]
    word = data[2 * i + 2]
    results.append(calculate_typing_time(keyboard, word))
for result in results:
    print(result)
