#!/usr/bin/env python3

class Planet(object):
    def __init__(self, name):
        self.name = name
        self.parents = []
        self.child = None
        self.visited = False

    def has_child(self):
        return self.child is not None
    
    def add_parent(self, parent):
        self.parents.append(parent)

    def __eq__(self, other):
        return self.name == other.name
    
    def __hash__(self):
        return hash(self.name)


class OrbitMap(object):
    def __init__(self, orbits):
        self.planets = {}
        self.__process_orbits(orbits)
    
    def count_total_orbits(self):
        total = 0
        for key in self.planets.keys():
            total += self.count_orbits(self.planets[key].name)
        return total

    def count_orbits(self, planet_name):
        planet = self.planets[planet_name]
        if planet.child is not None:
            return self.count_orbits(planet.child) + 1
        return 0

    def count_transfers(self, planet, target_planet):
        _planet = self.planets[planet]
        _target_planet = self.planets[target_planet]
        if _planet.name == _target_planet.name:
            return 0
        if not _planet.visited:
            _planet.visited = True
            if _planet.has_child():
                r = self.count_transfers(_planet.child, target_planet)
                if r >= 0:
                    return r+1
            for parent in _planet.parents:
                r = self.count_transfers(parent, target_planet)
                if r >= 0:
                    return r+1
        return -1

    def __process_orbits(self, orbits):
        for orbit in orbits:
            left = orbit.split(")")[0]
            right = orbit.split(")")[1]
            if left in self.planets:
                planet_child = self.planets[left]
            else: 
                planet_child = Planet(left)
                self.planets[left] = planet_child
            if right in self.planets:
                planet_parent = self.planets[right]
            else:
                planet_parent = Planet(right)
                self.planets[right] = planet_parent
            planet_parent.child = planet_child.name
            planet_child.add_parent(planet_parent.name)



if __name__ == "__main__":
    with open("input") as f:
        orbits = f.read().splitlines()
    map = OrbitMap(orbits)
    print(map.count_total_orbits()) # part1
    print(map.count_transfers("YOU", "SAN") - 2) #part2    
            