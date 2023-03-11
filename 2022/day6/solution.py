with open("input.txt", "r") as f:
    stream = f.read()
    for i in range(3, len(stream)):
        chunk = {stream[i], stream[i-1], stream[i-2], stream[i-3]}
        if len(chunk) == 4:
            print(i + 1)
            break
        
# part2
with open("input.txt", "r") as f:
    stream = f.read()
    for i in range(15, len(stream)):
        chunk = set(list(stream[i:-len(stream)+(i-14):-1]))
        if len(chunk) == 14:
            print(i + 1)
            break