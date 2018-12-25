import time


def problem36(max_number: int) -> int:
    return sum([int(x) for x in range(max_number - 1) if is_palindrome(str(x)) and is_palindrome(get_raw_bin(x))])


def get_raw_bin(number: int) -> str:
    return bin(number)[2:].lstrip("0")


def is_palindrome(number: str) -> bool:
    return number[::-1] == number


if __name__ == '__main__':
    startTime = time.time()
    solution = problem36(1000000)
    execTime = time.time() - startTime
    print('Solution: {0}'.format(solution))
    print('Exec-Time: {0}s'.format(execTime))
