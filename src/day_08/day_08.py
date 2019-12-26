import re
from functools import reduce


def get_layer_with_fewest_zero_digits(image_data: str, width: int, height: int):
    layer_length = width * height
    layers = [image_data[i: i + layer_length] for i in range(0, len(image_data), layer_length)]
    zeros_in_layer = list(map(lambda layer: len(re.findall('0', layer)), layers))
    return layers[zeros_in_layer.index(reduce(lambda a, b: a if a < b else b, zeros_in_layer))]


def get_ones_multiplied_by_twos(layer: str):
    return len(re.findall('1', layer)) * len(re.findall('2', layer))


def get_ones_multiplied_by_twos_from_fewest_zero_digits_layer(image_data: str, width: int, height: int):
    layer = get_layer_with_fewest_zero_digits(image_data, width, height)
    return get_ones_multiplied_by_twos(layer)


if __name__ == '__main__':
    with open('src/day_08/day_08.txt', 'r') as file:
        image_data = file.read()
    width, height = 25, 6
    ones_multiplied_by_twos_from_fewest_zero_digits_layer = get_ones_multiplied_by_twos_from_fewest_zero_digits_layer(image_data, width, height)
    print(f'Part one: {ones_multiplied_by_twos_from_fewest_zero_digits_layer}')    
