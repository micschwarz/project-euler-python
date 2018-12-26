import time


class Triangles:
    triangle_numbers = [1]
    max_triangle = 1


def problem42() -> int:
    words = [str(x).strip('"').lower() for x in open('words.txt', 'r').read().split(',')]
    return len([1 for w in words if is_triangle(get_alphabetic_val(w))]) - 1


def is_triangle(number: int) -> bool:
    if number == Triangles.max_triangle:
        return True

    if number < Triangles.max_triangle:
        return number in Triangles.triangle_numbers

    triangles = get_triangles(len(Triangles.triangle_numbers))
    for t in triangles:
        Triangles.triangle_numbers.append(t)
        Triangles.max_triangle = t
        if t == number:
            return True

        if t > number:
            return False


def get_triangles(start):
    n = start
    while True:
        yield int(n * 0.5 * (n + 1))
        n += 1


def get_alphabetic_val(word: str) -> int:
    return sum([int(ord(c) - 96) for c in word])


if __name__ == '__main__':
    startTime = time.time()
    solution = problem42()
    execTime = time.time() - startTime
    print('Solution: {0}'.format(solution))
    print('Exec-Time: {0}s'.format(execTime))
