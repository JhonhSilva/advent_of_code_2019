def get_parameters_modes_and_opcode(parameter: int):
    parameter = str(parameter)
    opcode = parameter[-2:]
    parameters_mode = parameter[:-2]
    parameters_mode = ('0' * (3 - len(parameters_mode))) + parameters_mode
    _, parameter2_mode, parameter1_mode = parameters_mode
    return [int(value) for value in [0, parameter2_mode, parameter1_mode, opcode]]


def get_value_by_parameter_mode(parameters: list, mode: int, parameter_value, relative_base: int):
    if mode == 0:
        return parameters[parameter_value]
    elif mode == 1:
        return parameter_value
    elif mode == 2:
        return parameters[relative_base + parameter_value]


def missing_memory(parameters: list, parameter_value: int):
    paramters_length = len(parameters) - 1
    if parameter_value >= paramters_length:
        return [0] * (parameter_value - paramters_length)
    return []


def execute_instructions(parameters: list, inputs: list = None) -> tuple:
    i = 0
    last_value = None
    relative_base = 0
    try:
        while True:
            # print('relative base:', relative_base)
            parameter = parameters[i]
            _, parameter2_mode, parameter1_mode, opcode = get_parameters_modes_and_opcode(parameter)
            print(parameter2_mode, parameter1_mode, opcode)
            if opcode in [1, 2, 7, 8]:
                p1, p2, p3 = parameters[i + 1], parameters[i + 2], parameters[i + 3]
                max_param = max(p1, p2, p3)
                parameters += missing_memory(parameters, max_param)
                parameter1 = get_value_by_parameter_mode(parameters, parameter1_mode, p1, relative_base)
                parameter2 = get_value_by_parameter_mode(parameters, parameter2_mode, p2, relative_base)
                parameter3 = get_value_by_parameter_mode(parameters, parameter2_mode, p3, relative_base)
                parameters, _ = operation(parameters, opcode, parameter1, parameter2, parameter3)
                i += 4
            elif opcode == 3:
                p1 = parameters[i + 1]
                parameters += missing_memory(parameters, p1)
                parameter1 = get_value_by_parameter_mode(parameters, parameter1_mode, p1, relative_base)
                parameters, _ = operation(parameters, opcode, parameter1, inputs=inputs)
                i += 2
            elif opcode == 4:
                p1 = parameters[i + 1]
                parameter1 = get_value_by_parameter_mode(parameters, parameter1_mode, p1, relative_base)
                parameters, _ = operation(parameters, opcode, parameter1, inputs=inputs)
                last_value = parameter1
                i += 2
            elif opcode in [5, 6]:
                p1, p2 = parameters[i + 1], parameters[i + 2]
                parameter1 = get_value_by_parameter_mode(parameters, parameter1_mode, p1, relative_base)
                parameter2 = get_value_by_parameter_mode(parameters, parameter2_mode, p2, relative_base)
                parameters, position = operation(parameters, opcode, parameter1, parameter2)
                i = i + 3 if position == 0 else position
            elif opcode == 9:
                p1 = parameters[i + 1]
                parameter1 = get_value_by_parameter_mode(parameters, parameter1_mode, p1, relative_base)
                relative_base += parameter1
                i += 2
            elif opcode == 99:
                return last_value, True
            else:
                i += 1
    except:
        return last_value, False


def operation(parameters: list, operation: int, parameter1: int, parameter2: int = 0, parameter3: int = 0, inputs: list = None) -> tuple:
    position = 0
    if operation == 1:
        parameters[parameter3] = parameter1 + parameter2
    elif operation == 2:
        parameters[parameter3] = parameter1 * parameter2
    elif operation == 3:
        parameters[parameter1] = int(input('Input value: ')) if inputs == None else inputs.pop(0)
    elif operation == 4:
        if inputs == None:
            print(f'Outupt value: {parameter1}')
    elif operation == 5:
        if parameter1 != 0:
            position = parameter2
    elif operation == 6:
        if parameter1 == 0:
            position = parameter2
    elif operation == 7:
        parameters[parameter3] = 1 if parameter1 < parameter2 else 0
    elif operation == 8:
        parameters[parameter3] = 1 if parameter1 == parameter2 else 0
    return parameters, position


if __name__ == '__main__':
    with open('src/day_09/day_09.txt', 'r') as file:
        parameters = list(map(int, file.read().split(',')))
    # parameters = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    # parameters = [1102,34915192,34915192,7,4,7,99,0]
    # parameters = [104,1125899906842624,99]
    execute_instructions(parameters)