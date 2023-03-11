import math

class Map:
    def __init__(self):
        self.movemap = [[0 for _ in range(801)] for _ in range(801)]
    
    def leave_trace(self, knot):
        self.movemap[400 - knot.y][400 - knot.x] = True
    
    def count_traces(self):
        return sum(list(map(sum, self.movemap)))

class Rope:
    def __init__(self, size, movemap):
        self.knots = []
        for i in range(size):
            if i == 0:
                self.knots.append(Knot(None)) # tail
            else:
                self.knots.append(Knot(self.knots[i-1]))
        self.head = self.knots[len(self.knots)-1]
        self.tail = self.knots[0]
        self.movemap = movemap
        self.leave_trace()
        
    def process_move(self, move):
        direction = move.split(' ')[0]
        steps = int(move.split(' ')[1])
        for i in range(steps):
            if direction == 'L':
                self.pull_left()
            elif direction == 'R':
                self.pull_right()
            elif direction == 'U':
                self.pull_up()
            elif direction == 'D':
                self.pull_down()
    
    def leave_trace(self):
        self.movemap.leave_trace(self.tail)

    def pull_left(self):    
        self.head.move_left()
        self.leave_trace()
    
    def pull_right(self):
        self.head.move_right()
        self.leave_trace()
    
    def pull_up(self):
        self.head.move_up()
        self.leave_trace()
    
    def pull_down(self):
        self.head.move_down()
        self.leave_trace()
        

class Knot:
    def __init__(self, child):
        self.child = child
        self.x = 0
        self.y = 0
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        if self.child and not self.neighbor(self.child):
            dx, dy = 0, 0
            if self.x > self.child.x:
                dx = 1
            elif self.x < self.child.x:
                dx = -1
            if self.y > self.child.y:
                dy = 1
            elif self.y < self.child.y:
                dy = -1
            self.child.move(dx, dy)
    
    def move_left(self):
        self.x -= 1
        if self.child and not self.neighbor(self.child):
            dx, dy = -1, 0
            if self.y > self.child.y:
                dy = 1
            elif self.y < self.child.y:
                dy = -1
            self.child.move(dx, dy)
    
    def move_right(self):
        self.x += 1
        if self.child and not self.neighbor(self.child):
            dx, dy = 1, 0
            if self.y > self.child.y:
                dy = 1
            elif self.y < self.child.y:
                dy = -1
            self.child.move(dx, dy)
    
    def move_up(self):
        self.y += 1
        if self.child and not self.neighbor(self.child):
            dx, dy = 0, 1
            if self.x > self.child.x:
                dx = 1
            elif self.x < self.child.x:
                dx = -1
            self.child.move(dx, dy)
    
    def move_down(self):
        self.y -= 1
        if self.child and not self.neighbor(self.child):
            dx, dy = 0, -1
            if self.x > self.child.x:
                dx = 1
            elif self.x < self.child.x:
                dx = -1
            self.child.move(dx, dy)
    
    def neighbor(self, another_knot):
         distance = math.sqrt(math.pow(another_knot.x - self.x, 2) + math.pow(another_knot.y - self.y, 2))
         return distance < 2

def solve(knot_size):
    with open("input.txt") as f:
        moves = f.read().splitlines()
        map = Map()
        rope = Rope(knot_size, map)
        for move in moves:
            rope.process_move(move)
        print(map.count_traces())

solve(2)
solve(10)