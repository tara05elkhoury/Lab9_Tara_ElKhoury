

import time
import unittest

from profiler import (
    slow_function,
    optimized_fast_function,
    memory_intensive_function,
)


class TestProfiler(unittest.TestCase):
    def time_function(self, func):
        start = time.perf_counter()
        result = func()
        duration = time.perf_counter() - start
        return result, duration

    def test_slow_function(self):
        result, duration = self.time_function(slow_function)
        print(f"slow_function executed in {duration:.6f} seconds.")
        self.assertEqual(result, 333_283_335_000)

    def test_fast_function(self):
        result, duration = self.time_function(optimized_fast_function)
        print(f"optimized_fast_function executed in {duration:.6f} seconds.")
        self.assertEqual(result, 328_350)

    def test_memory_intensive_function(self):
        result, duration = self.time_function(memory_intensive_function)
        print(f"memory_intensive_function executed in {duration:.6f} seconds.")
        self.assertEqual(result, 333_333_283_333_335_000_000)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
