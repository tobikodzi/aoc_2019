import re
import time


# part 1: 0.000997304916381836 s
def day_8():
    # part 1
    with open('inputs/input_day8.txt', mode='r') as file:
        encoded_image = file.read().strip()

    encoded_image_length = len(encoded_image)
    layer_size = 25*6
    layers_count = int(encoded_image_length / layer_size)

    image = []
    for i in range(layers_count):
        stop = layer_size * (i+1)
        start = stop - layer_size
        layer = encoded_image[start:stop]
        image.append(layer)

    fewest_zeros = min(image, key=lambda layer: layer.count('0'))
    print(fewest_zeros.count('1') * fewest_zeros.count('2'))

    # part 2
    # 0 is black, 1 is white, and 2 is transparent.
    final_image = []
    for i in range(layer_size):
        for j in range(layers_count):
            pixel = image[j][i]
            if pixel != '2':
                final_image.append(pixel)
                break

    for i in range(6*25):
        if final_image[i] == '1':
            print('#', end='')
        else:
            print(' ', end='')
        if i % 25 == 24:
            print()


def day_4():
    range = [int(num) for num in "153517 - 630395".split(sep=' - ')]
    for num in range:
        print(num)


# time: 0.1635301113128662 s
def day_3():
    # previous part 1: 8.4215726852417 s
    wires = open("inputs/input_day3.txt").readlines()
    wire_A, wire_B = [x.split(',') for x in wires]
    DX = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
    DY = {'L': 0, 'R': 0, 'U': 1, 'D': -1}

    def points(data):
        x = 0
        y = 0
        wire_points = set()
        for move in data:
            direction = move[0]
            steps = int(move[1:])
            for i in range(steps):
                x += DX[direction]
                y += DY[direction]
                wire_points.add((x, y))
        return wire_points

    wire_A_points = points(wire_A)
    wire_B_points = points(wire_B)
    intersects = wire_A_points & wire_B_points
    ans_end = min([abs(x) + abs(y) for (x, y) in intersects])
    print(ans_end)


# time: 1.8396062850952148 s
def day_2():
    def compute(index_1, index_2):
        content = open('inputs/input_day2.txt', mode='r').read()
        program = [int(x) for x in content.split(sep=',')]
        program[1] = index_1
        program[2] = index_2
        i = 0
        while program[i] != 99:
            a = program[i + 1]
            b = program[i + 2]
            c = program[i + 3]
            if program[i] == 1:
                program[c] = program[a] + program[b]
            elif program[i] == 2:
                program[c] = program[a] * program[b]
            i += 4
        return program[0]

    for i in range(0, 100):
        for j in range(0, 100):
            res = compute(index_1=i, index_2=j)
            if res == 19690720:
                print(res, 'is created with', i, j, 'solution is', 100*i+j)
                break


# time: 0.0009648799896240234 s
def day_1():
    def fuel(n):
        n = int(n / 3) - 2
        if n > 0:
            return n + (fuel(n))
        else:
            return 0

    content = open('inputs/input_day1.txt', mode='r').readlines()
    print('part 1:', sum([int(float(n) / 3) - 2 for n in content]))
    print('part 2:', sum([fuel(int(n)) for n in content]))


if __name__ == '__main__':
    start = time.time()
    # day_1()
    # day_2()
    # day_3()
    # day_4()
    day_8()
    end = time.time()
    print("time:", end - start, "s")
