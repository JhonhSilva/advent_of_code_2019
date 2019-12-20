from day_05 import execute_instructions


def get_output_signal(parameters: list, phase_setting: list):
    output = 0
    for phase in phase_setting:
        output = execute_instructions(parameters, inputs=[phase, output])
    return output


def get_highest_signal(parameters: list):
    highest_signal = 0
    phase_setting = None
    r = range(5)
    for a in r:
        for b in r:
            for c in r:
                for d in r:
                    for e in r:
                        phase = [a, b, c, d, e]
                        if len(set(phase)) < 5:
                            continue
                        signal = get_output_signal(parameters, phase)
                        phase_setting, highest_signal = (phase, signal) if signal > highest_signal else (phase_setting, highest_signal)
    return highest_signal, phase_setting


if __name__ == '__main__':
    with open('src/day_07/day_07.txt', 'r') as file:
        parameters = list(map(int, file.read().split(',')))
    highest_signal = get_highest_signal(parameters)
    print(f'Part one: {highest_signal}')
