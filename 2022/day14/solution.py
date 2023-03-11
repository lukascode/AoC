from itertools import cycle

class Cave:
    def __init__(self, size, part):
        self.part = part
        self.map = [['.' for i in range(size)] for j in range(size)]
        self.sand_start_pos_x = 500
        self.sand_start_pos_y = 0
        self.sand_count = 0
        self.last_rock = 0
        self.cave_floor = 0
        
    def place_rock(self, points):
        for i in range(0, len(points) - 1):
            self._place_rock(points[i], points[i + 1])
        self.cave_floor = self.last_rock + 2
    
    def _place_rock(self, start, stop):
        if start[0] != stop[0]:
            if self.last_rock < start[1]:
                self.last_rock = start[1]
            min_x = min([start[0],stop[0]])
            max_x = max([start[0],stop[0]])
            for x in range(min_x, max_x + 1):
                self.map[start[1]][x] = '#'
        else:
            min_y = min([start[1],stop[1]])
            max_y = max([start[1],stop[1]])
            for y in range(min_y, max_y + 1):
                self.map[y][start[0]] = '#'
                if self.last_rock < y:
                    self.last_rock = y
            
    
    def pour_sand(self):
        result = self._pour_sand(self.sand_start_pos_x, self.sand_start_pos_y)
        if result > 0:
            self.sand_count += result
        return result
    
    def _pour_sand(self, x, y):
        if self.map[y][x] in ['#', 'o']:
            return 0
        if self.part == 1:
            if y > self.last_rock:
             return -1
        else:
            if y + 1 == self.cave_floor:
                self.map[y][x] = 'o'
                return 1
        if self.map[y + 1][x] not in ['#', 'o']:
            return self._pour_sand(x, y + 1)
        elif self.map[y + 1][x - 1] not in ['#', 'o'] and (x - 1) >= 0:
            return self._pour_sand(x - 1, y + 1)
        elif self.map[y + 1][x + 1] not in ['#', 'o']:
            return self._pour_sand(x + 1, y + 1)
        else:
            self.map[y][x] = 'o'
            return 1

def solve(part):
    with open("input.txt") as f:
        cave = Cave(1201, part)
        lines = f.read().splitlines()
        for line in lines:
            points = []
            path = line.split('->')
            for point in path:
                x = int(point.split(',')[0])
                y = int(point.split(',')[1])
                points.append((x, y))
            cave.place_rock(points)
        
        result = 1
        while result > 0:
            result = cave.pour_sand()
        print(cave.sand_count)
        
solve(part=1)
solve(part=2)