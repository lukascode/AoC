
def is_contain(pair):
    left = pair.split(',')[0]
    right = pair.split(',')[1]
    left_a = int(left.split('-')[0])
    left_b = int(left.split('-')[1])
    right_a = int(right.split('-')[0])
    right_b = int(right.split('-')[1])
    return (left_a <= right_a and left_b >= right_b) or (right_a <= left_a and right_b >= left_b)

def overlap(pair):
    left = pair.split(',')[0]
    right = pair.split(',')[1]
    left_a = int(left.split('-')[0])
    left_b = int(left.split('-')[1])
    right_a = int(right.split('-')[0])
    right_b = int(right.split('-')[1])
    return left_b >= right_a and right_b >= left_a

with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    total = 0
    totalPart2 = 0
    for pair in lines:
        if is_contain(pair):
            total += 1
        if overlap(pair):
            totalPart2 += 1
    print(total)
    print(totalPart2)
    