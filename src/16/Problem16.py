import time


def problem16(exponent):
    cross_sum = 0

    num = 2 ** exponent
    while num > 0:
        cross_sum += num % 10
        num = num // 10

    return cross_sum


if __name__ == '__main__':
    startTime = time.time()
    solution = problem16(1000)
    execTime = time.time() - startTime
    print('Solution: {0}'.format(solution))
    print('Exec-Time: {0}s'.format(execTime))
