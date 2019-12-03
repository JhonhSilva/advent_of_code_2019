def get_positions(position: tuple, direction: str, distance: int):
    positions = []
    for i in range(1, distance + 1):
        x = position[0]
        y = position[1]
        if direction == 'U':
            y += i
        elif direction == 'R':
            x += i
        elif direction == 'D':
            y -= i
        else:
            x -= i
        positions.append((x, y))
    return positions


def get_cordinate(cordinate: str):
    return (cordinate[0].upper(), int(cordinate[1:]))


def execute_cordinates(cordinates: list):
    positions = [(0, 0)]
    for cordinate in cordinates:
        direction, distance = get_cordinate(cordinate)
        positions += get_positions(positions[-1], direction, distance)
    return positions[1:]


def get_intersections(line1: list, line2: list):
    return list(set(line1).intersection(line2))


def get_distances(intersections: list):
    distances = [abs(value[0]) + abs(value[1]) for value in intersections]
    distances.sort()
    return distances[0]


with open('python/src/day_03/day_03.txt') as file:
    lines = file.read().splitlines()
line1, line2 = [line.split(',') for line in lines]
cordinates1 = execute_cordinates(line1)
cordinates2 = execute_cordinates(line2)
intersections = get_intersections(cordinates1, cordinates2)
distance = get_distances(intersections)
print(f'Part one: {distance}')
