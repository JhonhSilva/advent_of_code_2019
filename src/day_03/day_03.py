def get_positions(position: tuple, direction: str, distance: int) -> list:
    positions = []
    for i in range(1, distance + 1):
        x, y = position[0], position[1]
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


def get_cordinate(cordinate: str) -> tuple:
    return (cordinate[0].upper(), int(cordinate[1:]))


def execute_cordinates(cordinates: list) -> list:
    positions = [(0, 0)]
    for cordinate in cordinates:
        direction, distance = get_cordinate(cordinate)
        positions += get_positions(positions[-1], direction, distance)
    return positions[1:]


def get_intersections(line1: list, line2: list) -> list:
    return list(set(line1).intersection(line2))


def get_closest_distance(intersections: list) -> int:
    distances = [abs(value[0]) + abs(value[1]) for value in intersections]
    distances.sort()
    return distances[0]


def get_fewest_combined_steps(cordinates1: list, cordinates2: list, intersections: list) -> int:
    return sorted([(cordinates1.index(intersection) + cordinates2.index(intersection)) + 2 for intersection in intersections ])[0]


with open('src/day_03/day_03.txt') as file:
    lines = file.read().splitlines()
line1, line2 = [line.split(',') for line in lines]
cordinates1 = execute_cordinates(line1)
cordinates2 = execute_cordinates(line2)
intersections = get_intersections(cordinates1, cordinates2)
closest_distance = get_closest_distance(intersections)
fewest_combined_steps = get_fewest_combined_steps(cordinates1, cordinates2, intersections)
print(f'Part one: {closest_distance}')
print(f'Part two: {fewest_combined_steps}')
