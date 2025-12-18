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

if __name__ == '__main__':
    print(part1())
