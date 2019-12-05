def execute_instructions(instructions: list) -> list:
    for i, instruction in enumerate(instructions):
        if i % 4 == 0:
            if instruction == 99:
                return instructions
            instructions = operation(instructions, instruction, instructions[i + 1], instructions[i + 2], instructions[i + 3])


def operation(instructions: list, operation: int, instruction1: int, instruction2: int, instruction3: int) -> list:
    instructions[instruction3] = instructions[instruction1] + instructions[instruction2] if operation == 1 else instructions[instruction1] * instructions[instruction2]
    return instructions


def set_noun_and_verb(instructions: list, noun: int, verb: int) -> list:
    instructions[1] = noun
    instructions[2] = verb
    return instructions


def find_noun_and_verb(instructions: list, expected_value: int) -> int:
    for noun in range(100):
        for verb in range(100):
            test = set_noun_and_verb(instructions[:], noun, verb)
            if execute_instructions(test)[0] == expected_value:
                return (100 * noun) + verb
    return None


instructions = []
with open('python/src/day_02/day_02.txt', 'r') as file:
    instructions = list(map(int, file.read().split(',')))
part_one = set_noun_and_verb(instructions[:], 12, 2)
part_one = execute_instructions(part_one)[0]
part_two = find_noun_and_verb(instructions[:], 19690720)
print(f'Part one: {part_one}')
print(f'Part two: {part_two}')
