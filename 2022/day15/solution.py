
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def distance(self, another_point):
        return abs(self.x - another_point.x) + abs(self.y - another_point.y)
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Beacon:
    def __init__(self, position, sensor):
        self.position = position
        self.sensor = sensor

class Sensor:
    def __init__(self, position, closest_beacon):
        self.position = position
        self.closest_beacon = Beacon(closest_beacon, self)
    
    def is_closer(self, another_beacon_position):
        current_distance = self.position.distance(self.closest_beacon.position)
        potential_distance = self.position.distance(another_beacon_position)
        return potential_distance <= current_distance

class Zone:
    def __init__(self):
        self.objects = {}
        self.sensors = []
        self.minx = float('inf')
        self.maxx = 0
    
    def add_sensor(self, sensor):
        self.sensors.append(sensor)
        
        if sensor.position.y in self.objects:
            self.objects[sensor.position.y].append(sensor)
        else:
            self.objects[sensor.position.y] = [sensor]
        if sensor.closest_beacon.position.y in self.objects:
            self.objects[sensor.closest_beacon.position.y].append(sensor.closest_beacon)
        else:
            self.objects[sensor.closest_beacon.position.y] = [sensor.closest_beacon]
            
        self.minx = min(self.minx, min(sensor.position.x, sensor.closest_beacon.position.x))
        self.maxx = max(self.maxx, max(sensor.position.x, sensor.closest_beacon.position.x))
    
    def check(self, y):
        total = 0
        minx = float('inf')
        maxx = 0
        for s in self.sensors:
            v_distance = abs(s.position.y - y)
            max_h_distance = s.position.distance(s.closest_beacon.position) - v_distance
            if max_h_distance >= 0:
                startx = s.position.x - max_h_distance
                endx = s.position.x + max_h_distance
                minx = min(minx, startx)
                maxx = max(maxx, endx)
        total += maxx - minx + 1
        
        for i in range(minx, maxx + 1):
            if self.is_occupied(Point(i, y)):
                total -= 1
        return total
            
    def is_occupied(self, point):
        if point.y in self.objects:
            obs = self.objects[point.y]
            for i in obs:
                if type(i) == Beacon and i.position.x == point.x:
                    return True
        return False        

with open("input.txt") as f:
    lines = f.read().splitlines()
    zone = Zone()
    for line in lines:
        sx = int(line.split(':')[0].split(' ')[2].split('=')[1].split(',')[0])
        sy = int(line.split(':')[0].split(' ')[3].split('=')[1])
        bx = int(line.split(':')[1].split(',')[0].split(' ')[5].split('=')[1])
        by = int(line.split(':')[1].split(',')[1].split('=')[1])
        zone.add_sensor(Sensor(position=Point(sx, sy),closest_beacon=Point(bx, by)))
    print(zone.check(2000000))
    
    
# part1 - 5564017