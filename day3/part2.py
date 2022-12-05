from itertools import zip_longest

with open("./input.txt", 'r') as data:
    lines = data.read().splitlines()

args = [iter(lines)] * 3
groups = zip_longest(*args)
priority = 0

for rucksack1, rucksack2, rucksack3 in groups:
    common_char = ''.join([
        char for char in rucksack1
        if char in rucksack2 and char in rucksack3])[0]
    if common_char.isupper():
        priority += ord(common_char) - ord('A') + 27
    else:
        priority += ord(common_char) - ord('a') + 1

print(priority)
