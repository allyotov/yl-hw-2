from typing import List


class CyclicIterator:
    def __init__(self, given_collection: List):
        self.current = 0
        self.length = len(given_collection)
        self.list = list(given_collection)

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        self.current %= self.length
        return self.current


if __name__ == '__main__':
    for iteration_num, element in enumerate(CyclicIterator(range(3))):
        print(element)
        if iteration_num > 100:
            break