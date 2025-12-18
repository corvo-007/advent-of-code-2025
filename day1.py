from read_file import read_file

file = read_file('input1.txt')

def part1():
    dial = 50
    count = 0

    for line in file:
        direction, rotations = line[0], int(line[1:].strip())

        if direction == 'L':
            rotations = -rotations
        
        dial = (dial + rotations) % 100

        if dial == 0:
            count += 1
    
    return count

def part2():
    dial = 50
    count = 0

    for line in file:
        direction, rotations = line[0], int(line[1:].strip())

        if rotations >= 100:
            count += rotations // 100
            rotations %= 100
        
        if direction == 'L':
            next_dial = dial - rotations

            if next_dial < 0:
                next_dial += 100
                if dial != 0:
                    count += 1
            dial = next_dial
        else:
            dial += rotations

            if dial > 100:
                count += 1
            dial %= 100
        
        if dial == 0:
            count += 1
    
    return count

if __name__ == '__main__':
    print(part1())
    print(part2())
