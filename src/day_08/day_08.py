import re
from functools import reduce


def get_layers(image_data: str, layer_length: int):
    return [image_data[i: i + layer_length] for i in range(0, len(image_data), layer_length)]


def get_layer_with_fewest_zero_digits(layers: list):
    zeros_in_layer = list(map(lambda layer: len(re.findall('0', layer)), layers))
    return layers[zeros_in_layer.index(reduce(lambda a, b: a if a < b else b, zeros_in_layer))]


def get_ones_multiplied_by_twos(layer: str):
    return len(re.findall('1', layer)) * len(re.findall('2', layer))


def get_ones_multiplied_by_twos_from_fewest_zero_digits_layer(image_data: str, width: int, height: int):
    layer_length = width * height
    layers = get_layers(image_data, layer_length)
    layer = get_layer_with_fewest_zero_digits(layers)
    return get_ones_multiplied_by_twos(layer)


def get_final_layer(layers: list):
    final_layer = layers[0]
    for layer in layers[1:]:
        for h, line in enumerate(layer):
            for w, pixel in enumerate(line):
                current_pixel = final_layer[h][w]
                if current_pixel == '2':
                    final_layer[h][w] = pixel
    return [''.join(line).replace('0', ' ') for line in final_layer]


def get_message(image_data: str, width: int, height: int):
    layer_length = width * height
    layers = get_layers(image_data, layer_length)
    formated_layers = list(map(lambda layer: list(map(list, get_layers(layer, width))), layers))
    return get_final_layer(formated_layers)


if __name__ == '__main__':
    with open('src/day_08/day_08.txt', 'r') as file:
        image_data = file.read()
    width, height = 25, 6
    ones_multiplied_by_twos_from_fewest_zero_digits_layer = get_ones_multiplied_by_twos_from_fewest_zero_digits_layer(image_data, width, height)
    final_layer = get_message(image_data, width, height)
    print(f'Part one: {ones_multiplied_by_twos_from_fewest_zero_digits_layer}')
    print('Part two: GJYEA\n')
    list(map(print, final_layer))
