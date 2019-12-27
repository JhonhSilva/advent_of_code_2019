from intcode import execute_instructions


def get_output_signal(parameters: list, phase_setting: list):
    output = 0
    for phase in phase_setting:
        output = execute_instructions(parameters, inputs=[phase, output])[0]
    return output


def get_loop_output_signal(parameters: list, phase_setting: list):
    phase_setting = list(map(lambda phase: [phase], phase_setting))
    phase_setting[0].append(0)
    i, all_finished = 0, []
    while True:
        current_phase_setting = phase_setting[i][:]
        output, finished = execute_instructions(parameters[:], inputs=current_phase_setting)
        all_finished.append(finished)
        i = i + 1 if i < len(phase_setting) - 1 else 0
        if sum(all_finished) == 5:
            return output
        phase_setting[i].append(output)
    return phase_setting[4][-1]


def get_highest_signal(parameters: list, phase_range: list, loop: bool = False):
    highest_signal = 0
    phase_setting = None
    for a in phase_range:
        for b in phase_range:
            for c in phase_range:
                for d in phase_range:
                    for e in phase_range:
                        phase = [a, b, c, d, e]
                        if len(set(phase)) < 5:
                            continue
                        signal = get_loop_output_signal(parameters, phase) if loop else get_output_signal(parameters, phase)
                        phase_setting, highest_signal = (phase, signal) if signal > highest_signal else (phase_setting, highest_signal)
    return highest_signal, phase_setting


if __name__ == '__main__':
    with open('src/day_07/day_07.txt', 'r') as file:
        parameters = list(map(int, file.read().split(',')))
    highest_signal = get_highest_signal(parameters, range(5))
    loop_highest_signal = get_highest_signal(parameters, range(5, 10), True)
    print(f'Part one: {highest_signal}')
    print(f'Part two: {loop_highest_signal}')
