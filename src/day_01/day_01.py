from math import floor


def get_fuel(mass: float) -> int:
    return floor(mass / 3) - 2


def get_fuel_fuel(fuel: float, total_fuel: float = 0) -> int:
    new_fuel = get_fuel(fuel)
    return get_fuel_fuel(new_fuel, total_fuel + new_fuel) if new_fuel > 0 else total_fuel


if __name__ == '__main__':
    with open('src/day_01/day_01.txt', 'r') as file:
        modules = list(map(int, file.read().splitlines()))

    fuel = sum(map(get_fuel, modules))
    total_fuel = sum(map(lambda f: f + get_fuel_fuel(f), map(get_fuel, modules)))
    print(f'Part one: {fuel}')
    print(f'Part two: {total_fuel}')
