#!/usr/bin/env python3


class coord(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_distance(self):
        return abs(self.x) + abs(self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return "[(" + str(self.x) + "," + str(self.y) + ") | " + str(self.get_distance()) + "]"


class wire(object):
    def __init__(self, path):
        self.path = path

    def intersect(self, other_wire):
        coords = {}
        for i in range(len(self.path)):
            coords[self.path[i]] = [1, i + 1, None]
        for i in range(len(other_wire.path)):
            key = other_wire.path[i]
            if key in coords and coords[key][2] is None:
                coords[key][0] += 1
                coords[key][2] = i + 1

        # [ ( { 2767, 312 }, 35106, 73976), ... ] 
        return list(map(lambda c: (c[0], c[1][1], c[1][2]), filter(lambda c: c[1][0] > 1, coords.items())))

    @staticmethod
    def from_steps(steps):
        return wire(wire.__process_steps(steps))

    @staticmethod
    def __process_steps(steps):
        x, y = 0, 0
        path = []
        for step in steps:
            direction = step[0]
            distance = int(step[1:])
            if direction == 'U':
                while distance > 0:
                    y += 1
                    distance -= 1
                    path.append(coord(x, y))
            elif direction == 'D':
                while distance > 0:
                    y -= 1
                    distance -= 1
                    path.append(coord(x, y))
            elif direction == 'R':
                while distance > 0:
                    x += 1
                    distance -= 1
                    path.append(coord(x, y))
            elif direction == 'L':
                while distance > 0:
                    x -= 1
                    distance -= 1
                    path.append(coord(x, y))
        return path


if __name__ == "__main__":
    with open("input") as f:
        data = f.readlines()
    steps1 = data[0].split(",")
    steps2 = data[1].split(",")

    w1 = wire.from_steps(steps1)
    w2 = wire.from_steps(steps2)

    r = w1.intersect(w2)

    r1 = sorted(r, key=lambda x: x[0].get_distance())
    r2 = sorted(r, key=lambda x: x[1] + x[2])

    print(r1[0][0].get_distance())
    print(r2[0][1] + r2[0][2])
