from intcode import execute_instructions


if __name__ == '__main__':
    with open('src/day_09/day_09.txt', 'r') as file:
        parameters = list(map(int, file.read().split(',')))
    execute_instructions(parameters)