
class Node:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
    
    def get_size(self):
        pass
        

class Directory(Node):
    def __init__(self, parent, name):
        super().__init__(parent, name)
        self.children = []
    
    def add_dir(self, name):
        dir = Directory(self, name)
        self.children.append(dir)
        return dir
    
    def add_file(self, name, size):
        file = File(self, name, size)
        self.children.append(file)
        return file
    
    def find_child(self, name):
        return next(filter(lambda ch: ch.name == name, self.children))
    
    def get_size(self):
        total = 0
        for child in self.children:
            total += child.get_size()
        return total
                

class File(Node):
    def __init__(self, parent, name, size):
        super().__init__(parent, name)
        self.size = size
    
    def get_size(self):
        return self.size
    
    
class FileSystemBuilder:
    def __init__(self):
        self.root = None
        self.cd = None
    
    def process_command(self, command):
        if command.startswith('$ cd'):
            name = command.split(' ')[2]
            if self.root == None:
                self.root = Directory(None, name)
                self.cd = self.root
            else:
                if name == '..':
                    self.cd = self.cd.parent
                else:
                    self.cd = self.cd.find_child(name)
        elif command.startswith('$ ls'):
            pass
        elif command.startswith('dir'):
            name = command.split(' ')[1]
            self.cd.add_dir(name)
        else:
            size = int(command.split(' ')[0])
            name = command.split(' ')[1]
            self.cd.add_file(name, size)
            
    def build(self):
        return FileSystem(self.root)
    

class FileSystem:
    def __init__(self, root):
        self.root = root
    
    def get_directories(self, size_condition):
        return FileSystem._get_directories(self.root, size_condition)
    
    @staticmethod
    def _get_directories(current_directory, size_condition):
        result = []
        if size_condition(current_directory.get_size()):
            result.append(current_directory)
        for child in current_directory.children:
            if type(child) == Directory:
                result.extend(FileSystem._get_directories(child, size_condition))
        return result
            
    
with open("input.txt") as f:
    commands = f.read().splitlines()
    builder = FileSystemBuilder()
    for command in commands:
        builder.process_command(command)
    fs = builder.build()
    dirs = fs.get_directories(lambda size: size <= 100000)
    total = 0
    for dir in dirs:
        total += dir.get_size()
    print(total)
    
    # part2
    total_size = fs.root.get_size()
    size_left = 70000000 - total_size
    size_needed = 30000000 - size_left
    dirs = fs.get_directories(lambda size: size >= size_needed)
    dirs = sorted(dirs, key=lambda dir: dir.get_size())
    print(dirs[0].get_size())