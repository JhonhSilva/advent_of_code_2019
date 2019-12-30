def modes_and_opcode(parameter: int) -> tuple:
    '''gets incode parameter and returns parameters modes and opcode\n
    args:\n        parameter: intcode parameter\n
    returns:\n        tuple of mode 3, mode 2, mode 1 and opcode'''
    parameter = f'{parameter:05}'
    (mode3, mode2, mode1), opcode = parameter[:-2], parameter[-2:]
    return tuple(map(int, (mode3, mode2, mode1, opcode)))


def value_by_mode(parameters: list, mode: int, value: int, base: int) -> int:
    if mode == 0:
        return parameters[value]
    elif mode == 1:
        return value
    elif mode == 2:
        return parameters[parameters[value] + base]


def additional_memory(parameters: list, value: int) -> list:
    parameters_length = len(parameters) - 1
    return [0] * (value - parameters_length) if value >= parameters_length else []


def execute_parameters(parameters: list, inputs: list = None) -> tuple:
    ni, position, base, last_value = 0, 0, 0, None
    try:
        while True:
            ci = ni
            parameter = parameters[ci]
            mode3, mode2, mode1, opcode = modes_and_opcode(parameter)

            p1, p2, p3 = 0, 0, 0
            if opcode in (1, 2, 3, 4, 5, 6, 7, 8, 9):
                p1 = value_by_mode(parameters, mode1, parameters[ci + 1], base)
                ni += 2
            if opcode in (1, 2, 5, 6, 7, 8):
                p2 = value_by_mode(parameters, mode2, parameters[ci + 2], base)
                ni += 1
            if opcode in (1, 2, 7, 8):
                p3 = value_by_mode(parameters, mode3, parameters[ci + 3], base)
                ni += 1

            max_value = max(p1, p2, p3)
            parameters += additional_memory(parameters, max_value)

            func = {1: int.__add__,
                    2: int.__mul__,
                    5: int.__ne__,
                    6: int.__eq__,
                    7: int.__lt__,
                    8: int.__eq__}.get(opcode, None)

            if opcode in (1, 2):
                parameters[p3] = func(p1, p2)
            elif opcode == 3:
                parameters[p1] = int(input('Input value: ')) if inputs == None else inputs.pop(0)
            elif opcode == 4:
                if inputs == None:
                    print(f'Outupt value: {p1}')
                last_value = p1
            elif opcode in (5, 6):
                position = p2 if func(p1, 0) else position
                ni = ni if position == 0 else position
            elif opcode in (7, 8):
                parameters[p3] = 1 if func(p1, p2) else 0
            elif opcode == 9:
                base += p1
            elif opcode == 99:
                return last_value, True
            else:
                raise Exception(f'Invalid opcode: {opcode}')
    except Exception as e:
        return last_value, False


if __name__ == '__main__':
    with open('src/day_09/day_09.txt', 'r') as file:
        parameters = list(map(int, file.read().split(',')))
    parameters = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
    # parameters = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
    # parameters = [104,1125899906842624,99]
    execute_parameters(parameters)
