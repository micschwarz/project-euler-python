import time


def problem22(filename: str) -> int:
    file = open(filename, 'r')
    names = sorted([str(name).strip('"').lower() for name in file.read().split(',')])

    total = 0
    for pos, name in enumerate(names):
        total += get_name_val(name) * (pos+1)

    return total


def get_name_val(name: str) -> int:
    val = 0
    for char in name:
        val += get_alphabetical_value(char)
    return val


def get_alphabetical_value(c: str) -> int:
    return ord(c) - 96


if __name__ == '__main__':
    startTime = time.time()
    solution = problem22('names.txt')
    execTime = time.time() - startTime
    print('Solution: {0}'.format(solution))
    print('Exec-Time: {0}s'.format(execTime))
