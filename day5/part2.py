
def execute_moves(stacks, moves):
    for (amount, start, dest) in moves:
        stacks[dest - 1].extend(stacks[start - 1][-amount:])
        del stacks[start - 1][-amount:]
    return stacks

def parse_stacks(raw_stacks):
    raw_stacks = raw_stacks.splitlines()
    num_stacks = int(raw_stacks[-1].split()[-1])
    stacks = [[] for _ in range(num_stacks)]
    width = num_stacks * 4 - 1
    for line in reversed(raw_stacks[:-1]):
        idx = 1
        while idx < width:
            if line[idx].isalpha():
                stacks[idx // 4].append(line[idx])
            idx += 4
    return stacks

def parse_moves(raw_moves):
    moves = []
    raw_moves = raw_moves.splitlines()
    for line in raw_moves:
        tokens = line.split(' ')
        moves.append([int(tokens[1]), int(tokens[3]), int(tokens[5])])
    return moves

with open("./input.txt", 'r') as data:
    raw_stacks, raw_moves = data.read().split('\n\n')

stacks, moves = parse_stacks(raw_stacks), parse_moves(raw_moves)
new_stacks = execute_moves(stacks, moves)
output = ''
for column in new_stacks:
    output += column[-1]
print(output)
