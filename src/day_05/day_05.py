def get_parameters_modes_and_opcode(parameter: int):
    parameter = str(parameter)
    opcode = parameter[-2:]
    parameters_mode = parameter[:-2]
    parameters_mode = ('0' * (3 - len(parameters_mode))) + parameters_mode
    _, parameter2_mode, parameter1_mode = parameters_mode
    return [int(value) for value in [0, parameter2_mode, parameter1_mode, opcode]]


def get_value_by_parameter_mode(instructions: list, mode: int, parameter_value):
    return instructions[parameter_value] if mode == 0 else parameter_value


def execute_instructions(parameters: list) -> list:
    i = 0
    while True:
        parameter = parameters[i]
        if i % 2 == 0:
            _, parameter2_mode, parameter1_mode, opcode = get_parameters_modes_and_opcode(parameter)
            if opcode in [1, 2]:
                parameter1 = get_value_by_parameter_mode(parameters, parameter1_mode, parameters[i + 1])
                parameter2 = get_value_by_parameter_mode(parameters, parameter2_mode, parameters[i + 2])
                parameter3 = parameters[i + 3]
                parameters = operation(parameters, opcode, parameter1, parameter2, parameter3)
                i += 4
            elif opcode in [3, 4]:
                parameters = operation(parameters, opcode, parameters[i + 1])
                i += 2
            elif opcode == 99:
                return parameters
            else:
                i += 1


def operation(parameters: list, operation: int, parameter1: int, parameter2: int = 0, parameter3: int = 0) -> list:
    if operation == 1:
        parameters[parameter3] = parameter1 + parameter2
    elif operation == 2:
        parameters[parameter3] = parameter1 * parameter2
    elif operation == 3:
        parameters[parameter1] = int(input('Insert a value: '))
    elif operation == 4:
        print(f'Value in position [{parameter1}]: {parameters[parameter1]}')
    return parameters


parameters = []
with open('src/day_05/day_05.txt', 'r') as file:
    parameters = list(map(int, file.read().split(',')))
part_one = execute_instructions(parameters)
