import math
import time


def problem20(n: int) -> int:
    return sum([int(x) for x in str(math.factorial(n))])


if __name__ == '__main__':
    startTime = time.time()
    solution = problem20(100)
    execTime = time.time() - startTime
    print('Solution: {0}'.format(solution))
    print('Exec-Time: {0}s'.format(execTime))