import time


class Triangle:
    def __init__(self):
        self.tree = self.get_tree('triangle.txt')

    def get_tree(self, filename: str) -> [[int]]:
        lines = []
        file = open(filename, 'r')
        for line in file:
            lines.append([int(n) for n in line.split(" ")])

        return lines

    def get_tree_val(self, index: int, line: int) -> int:
        if len(self.tree)-1 == line:
            return self.tree[line][index]

        if index < 0 or len(self.tree[line])-1 < index:
            return 0

        left_val = self.get_tree_val(index, line + 1)
        right_val = self.get_tree_val(index + 1, line + 1)

        return self.tree[line][index] + (left_val if left_val > right_val else right_val)

    def get_max_path(self) -> int:
        return self.get_tree_val(0, 0)


def problem18():
    return (Triangle()).get_max_path()


if __name__ == '__main__':
    startTime = time.time()
    solution = problem18()
    execTime = time.time() - startTime
    print('Solution: {0}'.format(solution))
    print('Exec-Time: {0}s'.format(execTime))
