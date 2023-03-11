
class Monkey:
    def __init__(self):
        self.inspections = 0
        
    def set_items(self, items):
        self.items = items
    
    def set_operation(self, operation):
        self.operation = operation
    
    def set_argument(self, argument):
        self.argument = argument
    
    def set_divisor(self, divisor):
        self.divisor = divisor
    
    def set_true_monkey(self, true_monkey):
        self.true_monkey = true_monkey
    
    def set_false_monkey(self, false_monkey):
        self.false_monkey = false_monkey
    
    def set_game(self, game):
        self.game = game
        
    def play(self):
        while self.items:
            item = self.items.pop(0)
            if self.operation == '+':
                item += self.argument
            elif self.operation == '*':
                item *= self.argument
            elif self.operation == '**':
                item **= 2
            # item //= 3 disabled for part2
            if item % self.divisor == 0:
                self.game.throw_item(self.true_monkey, item)
            else:
                self.game.throw_item(self.false_monkey, item)
            self.inspections += 1

    def add_item(self, item):
        self.items.append(item)
    
    def __str__(self):
        return f"{{items={self.items},operation={self.operation},argument={self.argument},divisor={self.divisor},true={self.true_monkey},false={self.false_monkey}}}"
        
class Game:
    def __init__(self, monkeys, number_of_rounds):
        self.monkeys = monkeys
        self.number_of_rounds = number_of_rounds
        self.modulo = 1
        for m in self.monkeys:
            m.set_game(self)
            self.modulo *= m.divisor
    
    def start_game(self):
        for i in range(self.number_of_rounds):
            for i, m in enumerate(self.monkeys):
                m.play()
    
    def top_monkeys(self):
        return sorted(self.monkeys, key = lambda m: m.inspections, reverse = True)[:2]
    
    def throw_item(self, monkey, item):
        self.monkeys[monkey].add_item(item % self.modulo)

def solve():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
        monkeys = []
        def current_monkey():
            return monkeys[-1]
        for line in lines:
            line = line.strip()
            if line.startswith("Monkey"):
                monkeys.append(Monkey())
            elif line.startswith("Starting items"):
                if line.split(':')[1]:
                    current_monkey().set_items(list(map(int, line.split(':')[1].split(','))))
                else:
                    current_monkey().set_items([])
            elif line.startswith("Operation"):
                operation = line.split(' ')[4]
                argument = line.split(' ')[5]
                if operation == '*' and argument == 'old':
                    operation = '**'
                else:
                    argument = int(argument)
                current_monkey().set_operation(operation)
                current_monkey().set_argument(argument)
            elif line.startswith("Test"):
                current_monkey().set_divisor(int(line.split(' ')[3]))
            elif line.startswith("If true"):
                current_monkey().set_true_monkey(int(line.split(' ')[5]))
            elif line.startswith("If false"):
                current_monkey().set_false_monkey(int(line.split(' ')[5]))
                  
        game = Game(monkeys, 10000)
        game.start_game()
        top_monkeys = game.top_monkeys()
        print(top_monkeys[0].inspections * top_monkeys[1].inspections)
                
solve()
