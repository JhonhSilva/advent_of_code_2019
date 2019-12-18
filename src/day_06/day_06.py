class planet(object):
    def __init__(self, name: str):
        self.name = name
        self.planets = []


    def add(self, planet: object) -> object:
        self.planets.append(planet)
        return self


    def print(self, level: int) -> str:
        level += 1
        identation = (' ' * 6) * level
        s = f'{identation}{level}: {self.name}\n'
        for planet in self.planets:
            s += planet.print(level)
        return s
    

    def __repr__(self) -> str:
        return f'{self.name}: {self.planets}'


    def __str__(self) -> str:
        return self.print(-1)


    def get_total_orbit(self, start: int) -> int:
        total = start + 1
        return total + sum(map(lambda planet: planet.get_total_orbit(total), self.planets))


def get_all_planets(lines: list) -> dict:
    all_planets = {}
    for line in lines:
        center, orbit_planet = line.split(')')
        all_planets[center] = planet(center)
        all_planets[orbit_planet] = planet(orbit_planet)
    return all_planets


def get_orbits(all_planets: dict, lines: list) -> dict:
    for line in lines:
        center, orbit_planet = line.split(')')
        all_planets[center] = all_planets[center].add(all_planets[orbit_planet])
    return all_planets['COM']


with open('src/day_06/day_06.txt') as file:
    lines = file.read().splitlines()
all_planets = get_all_planets(lines)
orbits = get_orbits(all_planets, lines)
total_orbits = orbits.get_total_orbit(-1)
print(f'Part one: {total_orbits}')
