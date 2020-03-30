#!/usr/bin/env python3

import sys
import random
import math
import collections

def calc_func(x0, y0, x1, y1):
    if x0 != x1:
        a = (y0 - y1) / (x0 - x1)
        b = (x0*y1 - x1*y0) / (x0 - x1)
        return (a, b)
    return x0

def calc_distance(x0, y0, x1, y1):
    return math.sqrt((x1 - x0)**2.0 + (y1 - y0)**2.0)

def calc_minimum_distance_point(laser_position, points):
    min_distance = None
    min_distance_point = None
    f = False
    for point in points:
        distance = calc_distance(laser_position[0], laser_position[1], point[0], point[1])
        if min_distance is None or distance < min_distance:
            min_distance = distance
            min_distance_point = point
    return min_distance_point


def calc_detect_number(x, y):
    def get_index(x, y, j, i):
        if i < y:
            return 0
        elif i > y:
            return 1
        else:
            if j < x:
                return 0
            elif j > x:
                return 1
    fx_collection = {}
    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            if (x, y) != (j, i):
                if map_data[i][j] == '#':
                    fx = calc_func(x, y, j, i)
                    if fx in fx_collection:
                        fx_collection[fx][get_index(x, y, j, i)].append((j, i))
                    else:
                        fx_collection[fx] = [[], []]
                        fx_collection[fx][get_index(x, y, j, i)].append((j, i))
    total = 0
    for k in fx_collection.keys():
        if len(fx_collection[k][0]) > 0:
            total += 1
        if len(fx_collection[k][1]) > 0:
            total += 1
    return total


def part1():
    max_detection = None
    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            if map_data[i][j] == '#':
                n = calc_detect_number(j, i)
                if max_detection is None or max_detection < n:
                    max_detection = n
    print(max_detection)

def part2():
    laser_position = (17, 23)
    lp = (laser_position[0], len(map_data) - laser_position[1] - 1)

    angles = {}
    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            if (j, i) != laser_position:
                if map_data[i][j] == '#':
                    x, y = j, len(map_data) - i - 1
                    angle = math.atan2(y - lp[1], x - lp[0])
                    if angle in angles:
                        angles[angle].append((x, y))
                    else:
                        angles[angle] = [(x, y)]

    # sort
    angles_tmp = sorted(list(angles.keys()))

    # start from pi / 2
    for i, v in enumerate(angles_tmp):
        if v >= math.pi / 2.0:
            tmp = angles_tmp[:i]
            tmp.reverse()
            tmp2 = angles_tmp[i+1:]
            tmp2.reverse()
            angles_tmp = [angles_tmp[i]] + tmp + tmp2
            break

    vaporized_points = []

    while len(angles) > 0:
        for angle in angles_tmp:
            if angle in angles:
                points = angles[angle]
                if len(points) > 0:
                    point = calc_minimum_distance_point(lp, points)
                    map_x, map_y = point[0], len(map_data) - point[1] - 1
                    map_data[map_y][map_x] = '.'
                    points.remove(point)
                    vaporized_points.append((map_x, map_y))
                else:
                    del angles[angle]
        
    print(vaporized_points[199])

if __name__ == "__main__":
    with open("input") as f:
        data = f.read().splitlines()
        map_data = []
        for line in data:
            map_data.append([ch for ch in line.strip()])

        part1()
        part2()

        




        
