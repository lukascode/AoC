
elfs = [0]

with open("input.txt") as f:
    lines = f.read().splitlines()
    for l in lines:
        if l.strip():
            elfs[len(elfs)-1] += int(l)
        else:
            elfs.append(0)
            
print(max(elfs))
print(sum(sorted(elfs, reverse=True)[:3]))