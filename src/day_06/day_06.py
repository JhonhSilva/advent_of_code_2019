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


    def get_total_orbit(self, start: int = -1) -> int:
        total = start + 1
        return total + sum(map(lambda planet: planet.get_total_orbit(total), self.planets))


    def get_minimum_orbital_transfers(self, p1: str, p2: str):
        p = self.get_minimum_common_orbit(p1, p2)
        p1_distance = p.get_distance_from_root_to(p1)
        p2_distance = p.get_distance_from_root_to(p2)
        return (p1_distance + p2_distance) - 2


    def get_distance_from_root_to(self, p: str, count: int = -1):
        count += 1
        return count if self.name.lower() == p.lower() else sum(map(lambda planet: planet.get_distance_from_root_to(p, count), self.planets))


    def get_minimum_common_orbit(self, p1: str, p2: str, last_planet = None):
        if last_planet == None:
            last_planet = self
        if self.has_planet(p1) and self.has_planet(p2):
            for planet in self.planets:
                r = planet.get_minimum_common_orbit(p1, p2, self)
                if r.name != self.name:
                    return r
            return self
        else:
            return last_planet


    def has_planet(self, planet_name: str):
        return planet_name == self.name or any(map(lambda planet: planet.has_planet(planet_name), self.planets))
    

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
total_orbits = orbits.get_total_orbit()
minimum_orbital_transfers = orbits.get_minimum_orbital_transfers('YOU', 'SAN')
print(f'Part one: {total_orbits}')
print(f'Part two: {minimum_orbital_transfers}')
