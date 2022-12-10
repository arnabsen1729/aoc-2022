from enum import Enum

ANSWER = 13140
CYCLE_LIMIT = 220

class COMMANDS(Enum):
    NOOP = 'noop'
    ADDX = 'addx'

CYCLES = {
    COMMANDS.NOOP: 1,
    COMMANDS.ADDX: 2,
}

def parse(lines: list[str]) -> list[list[str]]:
    commands = []
    for line in lines:
        command = line.strip().split()
        if len(command) == 2:
            command[1] = int(command[1])
        
        if command[0] == 'noop':
            command[0] = COMMANDS.NOOP
        elif command[0] == 'addx':
            command[0] = COMMANDS.ADDX

        commands.append(command)
    return commands

def part1(cmds: list[list[str]]):
    intervals = 20 # for update intervals += 40
    cycle = 0
    singal_strength = 0
    command_index = 0
    current_command = cmds[0][0]
    current_command_cycles = CYCLES[current_command]
    X = 1

    while cycle <= CYCLE_LIMIT:
        cycle += 1
        current_command_cycles -= 1

        # cheching signal strength
        if cycle == intervals:
            singal_strength += cycle*X
            intervals += 40

        # executing commands
        if current_command_cycles == 0:
            if current_command == COMMANDS.ADDX:
                X += cmds[command_index][1]

            command_index += 1
            if command_index == len(cmds):
                break

            current_command = cmds[command_index][0]
            current_command_cycles = CYCLES[current_command]

    return singal_strength

def main():
    global f
    f = open('test.txt')
    lines = f.readlines()
    data = parse(lines)
    assert part1(data) == ANSWER
    f.close()

    f = open('input.txt')
    lines = f.readlines()
    data = parse(lines)
    print('Part 1:', part1(data))
    f.close()

if __name__ == '__main__':
    main()