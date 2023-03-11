import queue

map = []

class Elevation:
    def __init__(self, letter, x, y):
        self.x = x
        self.y = y
        self.start = False
        self.end = False
        if letter == 'S':
            self.start = True
            self.letter = 'a'
        elif letter == 'E':
            self.end = True
            self.letter = 'z'
        else:
            self.letter = letter
            
        self.neighbours = []
        self.reset()
        
    def reset(self):
        self.visited = False
        self.current_distance = float("inf")
        self.previous = None
    
    def process_neighbours(self):
        if self.y - 1 >= 0:
            self.add_neighbour(map[self.y - 1][self.x])
        if self.y + 1 < len(map):
            self.add_neighbour(map[self.y + 1][self.x])
        if self.x - 1 >= 0:
            self.add_neighbour(map[self.y][self.x - 1])
        if self.x + 1 < len(map[self.y]):
            self.add_neighbour(map[self.y][self.x + 1])
    
    def add_neighbour(self, elevation):
        if self.is_neighbour(elevation):
            self.neighbours.append(elevation)
    
    def is_neighbour(self, elevation):
        return ord(self.letter) - ord(elevation.letter) >= -1
            
    def __lt__(self, other):
        return self.current_distance < other.current_distance
    
    def __repr__(self):
        return f"letter={self.letter},x={self.x},y={self.y},nsize={len(self.neighbours)},start={self.start},end={self.end},visited={self.visited}"

def find_shortest_path(node):
    node.current_distance = 0
    pq = queue.PriorityQueue()
    pq.put(node)
    end = None
    while not pq.empty():
        current_node = pq.get()
        if current_node.visited:
            continue
        if current_node.end:
            end = current_node
            current_node.visited = True
            continue
        for n in current_node.neighbours:
            if not n.visited:
                distance = n.current_distance
                if current_node.is_neighbour(n):
                    distance = current_node.current_distance + 1
                if distance < n.current_distance:
                    n.current_distance = distance
                    n.previous = current_node
                pq.put(n)
        current_node.visited = True

    if end:
        current_node = end
        path = ""
        while current_node:
            path += current_node.letter
            current_node = current_node.previous
        return path
    else:
        return "Not found"
    
def parse():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
        start = None
        for line in lines:
            row = []
            for elevation in line:
                x, y = len(row), len(map)
                e = Elevation(elevation, x, y)
                if e.start:
                    start = e
                row.append(e)      
            map.append(row)
        
        for i in map:
            for elevation in i:
                elevation.process_neighbours()
    
        return start

def reset_map():
    for i in map:
        for j in i:
            j.reset()

def solve():     
    start = parse()
    print(len(find_shortest_path(start))-1)
    
    # part2
    lengts = []
    for row in map:
        for node in row:
            if node.letter == 'a':
                reset_map()
                path = find_shortest_path(node)
                if path != 'Not found':
                    lengts.append(len(path)-1)
    print(min(lengts))
    
solve()
    
   
    