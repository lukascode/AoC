stacks = [
    ['W', 'M', 'L', 'F'],
    ['B', 'Z', 'V', 'M', 'F'],
    ['H', 'V', 'R', 'S', 'L', 'Q'],
    ['F', 'S', 'V', 'Q', 'P', 'M', 'T', 'J'],
    ['L', 'S', 'W'],
    ['F', 'V', 'P', 'M', 'R', 'J', 'W'],
    ['J', 'Q', 'C', 'P', 'N', 'R', 'F'],
    ['V', 'H', 'P', 'S', 'Z', 'W', 'R', 'B'], 
    ['B', 'M', 'J', 'C', 'G', 'H', 'Z', 'W']
]

def process_line(line):
    tokens = line.split(' ')
    count = int(tokens[1])
    source_stack = int(tokens[3]) - 1
    target_stack = int(tokens[5]) - 1
    for i in range(count):
        val = stacks[source_stack].pop()
        stacks[target_stack].append(val)
        
def process_line_part2(line):
    tokens = line.split(' ')
    count = int(tokens[1])
    source_stack = int(tokens[3]) - 1
    target_stack = int(tokens[5]) - 1
    result_block = []
    for i in range(count):
        result_block.insert(0, stacks[source_stack].pop())
    stacks[target_stack].extend(result_block)

with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    for line in lines:
        process_line_part2(line)
        #process_line(line)
    result = ''
    for stack in stacks:
        result += stack[-1]
    print(result)
    