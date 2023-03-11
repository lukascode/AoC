
def calculate_priority(c):
    if c.islower():
        return ord(c) % 97 + 1
    else:
        return ord(c) % 65 + 27

with open("input.txt") as f:
    lines = f.read().splitlines()
    total = 0
    for l in lines:
        first_half = l[:len(l)//2]
        second_half = l[len(l)//2:]
        for c in first_half:
            if second_half.find(c) != -1:
                total += calculate_priority(c)
                break
    print(total)

# part2
with open("input.txt") as f:
    lines = f.read().splitlines()
    total = 0
    for i in range(0, len(lines), 3):
        group = lines[i:i+3]
        for c in group[0]:
            if group[1].find(c) >= 0 and group[2].find(c) >= 0:
                total +=  calculate_priority(c)
                break
    print(total)