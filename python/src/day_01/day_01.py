from math import floor
import pandas as pd


def get_fuel(mass: float):
    return floor(mass / 3) - 2


def get_fuel_fuel(fuel: float, total_fuel: float = 0):
    new_fuel = get_fuel(fuel)
    return get_fuel_fuel(new_fuel, total_fuel + new_fuel) if new_fuel > 0 else total_fuel


modules = pd.read_csv('python/src/day_01/day_01.csv', names=['module'])
fuel = modules.module.apply(get_fuel).sum()
total_fuel = modules.module.apply(get_fuel).apply(lambda f: f + get_fuel_fuel(f)).sum()
print(f'Part one: {fuel}')
print(f'Part two: {total_fuel}')
