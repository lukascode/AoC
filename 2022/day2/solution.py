
# 0 lost, 3 draw, 6 won
# 1 rock, 2 paper, 3 scissors


# OP
# A rock, B paper, C scissors

# ME
# X rock, Y paper, Z scissors


points = {
    'A X': 3 + 1,
    'A Y': 6 + 2,
    'A Z': 0 + 3,
    'B X': 0 + 1,
    'B Y': 3 + 2,
    'B Z': 6 + 3,
    'C X': 6 + 1,
    'C Y': 0 + 2,
    'C Z': 3 + 3
}

# OP
# A rock, B paper, C scissors
# X lose, Y draw, Z win

# ME
# X rock, Y paper, Z scissors

part2_moves = {
    'A X': 'A Z',
    'A Y': 'A X',
    'A Z': 'A Y',
    'B X': 'B X',
    'B Y': 'B Y',
    'B Z': 'B Z',
    'C X': 'C Y',
    'C Y': 'C Z',
    'C Z': 'C X'
}


with open("input.txt") as f:
    rounds = f.read().splitlines()
    totalScore = 0
    totalScorePart2 = 0
    for round in rounds:
        totalScore += points[round]
        totalScorePart2 += points[part2_moves[round]]
    print(totalScore)
    print(totalScorePart2)
        