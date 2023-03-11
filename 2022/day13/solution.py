import ast

class Pair:
    def __init__(self, left, right):
        self.left = ast.literal_eval(left)
        self.right = ast.literal_eval(right)
    
    def is_in_right_order(self):
        return self._check_order(self.left, self.right) == 1
    
    def _check_order(self, left, right):
        for i in range(min(len(left), len(right))):
            l, r = left[i], right[i]
            if type(l) == list and type(r) == list:
                right_order = self._check_order(l, r)
                if right_order != 0:
                    return right_order
            elif type(l) == list:
                right_order = self._check_order(l, [r])
                if right_order != 0:
                    return right_order
            elif type(r) == list:
                right_order = self._check_order([l], r)
                if right_order != 0:
                    return right_order
            else:
                if l < r:
                    return 1
                elif l > r:
                    return -1
                
        if len(left) < len(right):
            return 1
        elif len(left) > len(right):
            return -1
        else:
            return 0

class Chunk:
    def __init__(self, data):
        self.data = data
    
    def __eq__(self, other):
        return self.data == other.data
    
    def __lt__(self, other):
        return Pair(self.data, other.data).is_in_right_order()
    
    def __repr__(self):
        return str(self.data)

with open("input.txt") as f:
    lines = list(filter(lambda l: l.strip(), f.read().splitlines()))
    pairs = []
    for i in range(0, len(lines) - 1, 2):
        left = lines[i]
        right = lines[i + 1]
        pairs.append(Pair(left, right))
        
    total = 0
    for i, p in enumerate(pairs):
        if p.is_in_right_order():
            total += i + 1
    print(total)
    
    #part2
    pairs.append(Pair("[[2]]", "[[6]]"))
    signal = []
    for p in pairs:
        signal.append(Chunk(str(p.left)))
        signal.append(Chunk(str(p.right)))
    signal = sorted(signal)
    print((signal.index(Chunk("[[2]]"))+1) * (signal.index(Chunk("[[6]]"))+1))
    
    
        