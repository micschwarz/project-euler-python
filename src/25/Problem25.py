import math
import time


def problem22(digits: int) -> int:
    exponent = digits - 1
    golden_ratio = (1 + 5 ** 0.5) / 2

    return math.floor((math.log(10) * exponent + math.log(5)/2)/(math.log(golden_ratio))) + 1


if __name__ == '__main__':
    startTime = time.time()
    solution = problem22(1000)
    execTime = time.time() - startTime
    print('Solution: {0}'.format(solution))
    print('Exec-Time: {0}s'.format(execTime))
