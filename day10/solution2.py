from enum import Enum

CYCLE_LIMIT = 240

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

def solve(cmds: list[list[str]]):
    cycle = 0
    command_index = 0
    current_command = cmds[0][0]
    current_command_cycles = CYCLES[current_command]

    output = ''

    X = 1

    while cycle <= CYCLE_LIMIT:
        cycle += 1
        current_command_cycles -= 1

        if (cycle-1)%40 in [X-1, X, X+1]:
            # print(f'draws # {cycle}, X is {X}')
            output += '█'
        else:
            # print(f'draws . {cycle}, X is {X}')
            output += ' '

        # executing commands
        if current_command_cycles == 0 and command_index != len(cmds):
            if current_command == COMMANDS.ADDX:
                X += cmds[command_index][1]
                # print(f'x updated to {X}')

            command_index += 1
            if command_index == len(cmds):
                break

            current_command = cmds[command_index][0]
            current_command_cycles = CYCLES[current_command]

    # split output into lines each of 40
    lines = [output[i:i+40] for i in range(0, len(output), 40)]
    for line in lines:
        print(line)


def main():
    global f
    # f = open('test.txt')
    # lines = f.readlines()
    # data = parse(lines)
    # solve(data)
    # f.close()

    f = open('input.txt')
    lines = f.readlines()
    data = parse(lines)
    solve(data)
    f.close()

if __name__ == '__main__':
    main()