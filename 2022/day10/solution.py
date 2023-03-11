
class Crt:
    def __init__(self):
        self.buffer = [['.' for _ in range(40)] for _ in range(6)]
        self.x = 0
        self.y = 0
    
    def draw_pixel(self, sprite_position):
        if self.x in [sprite_position - 1, sprite_position, sprite_position + 1]:
            self.buffer[self.y][self.x] = '#'
        if self.x < 39:
            self.x += 1
        else:
            self.x = 0
            if self.y < 5:
                self.y += 1
    
    def render(self):
        for i in self.buffer:
            for j in i:
                print(j, end='')
            print()

class Processor:
    def __init__(self, crt):
        self.x = 1
        self.cycle = 0
        self.crt = crt
        self.signal_strengths = []
    
    def total_strength(self):
        return sum(self.signal_strengths)
    
    def process(self, instruction):
        if instruction == "noop":
            self._next_cycle()
        elif instruction.startswith("addx"):
            self._next_cycle()
            dx = int(instruction.split(' ')[1])
            self._next_cycle()
            self.x += dx
    
    def _next_cycle(self):
        self.cycle += 1
        if self.cycle in [20, 60, 100, 140, 180, 220]:
            self.signal_strengths.append(self.x * self.cycle)
        self.crt.draw_pixel(self.x)
    
with open("input.txt") as f:
    instructions = f.read().splitlines()
    crt = Crt()
    processor = Processor(crt)
    for i in instructions:
        processor.process(i)
    print(processor.total_strength())
    crt.render()
    