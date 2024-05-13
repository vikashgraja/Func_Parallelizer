"""
Test case for func_parallelizer
"""

import time
import func_parallelizer


class Calculate:
    """

    """
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        """
        Function to add 2 numbers
        """
        s = self.a + self.b
        return s

    def mul(self):
        """
        Function to multiply 2 numbers
        """
        p = self.a * self.b
        return p


if __name__ == '__main__':
    calculation = Calculate(10, 20)
    tasks = [
        calculation.add,
        calculation.mul,
    ]

    print('start')
    start = time.time()
    print(func_parallelizer.all_cores)
    results = func_parallelizer.parallel_runner(tasks, cpu_cores=2)
    print(results)
    end = time.time()
    print('Time', end - start)
