#!/usr/bin/env python3

width, height = 25, 6

def count_digits(layer, digit):
    total = 0
    for d in layer:
        if d == digit:
            total += 1
    return total

def solve_part1(layers):
    layer_min, layer_min_value = None, None
    for layer in layers:
        total_zeros = count_digits(layer, 0)
        if layer_min_value is None or total_zeros < layer_min_value:
            layer_min = layer
            layer_min_value = total_zeros  
    print(count_digits(layer_min, 1) * count_digits(layer_min, 2))

def solve_part2(layers):
    layer_size = width * height
    result = []
    for i in range(layer_size):
        for layer in layers:
            if layer[i] != 2:
                digit = layer[i]
                break
        result.append(digit)
    result = [result[i:i+width] for i in range(0, len(result), width)]
    for line in result:
        print(''.join(list(map(lambda x: str(x), line))))
        

if __name__ == "__main__":
    with open("input") as f:
        data = f.read().splitlines()[0]
        digits = []
        for d in data:
            digits.append(d)
        digits = list(map(lambda d: int(d), digits))
        layer_size = width * height
        layers = [digits[i:i+layer_size] for i in range(0, len(digits), layer_size)]
        solve_part1(layers)
        solve_part2(layers)
        
            

