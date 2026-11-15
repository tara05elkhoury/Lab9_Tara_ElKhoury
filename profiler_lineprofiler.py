

from line_profiler import LineProfiler


def slow_function():
    n = 10_000
    return n * (n - 1) * (2 * n - 1) // 6


def optimized_fast_function():
    n = 100
    return n * (n - 1) * (2 * n - 1) // 6


def memory_intensive_function():
    n = 10_000_000
    return n * (n - 1) * (2 * n - 1) // 6


def main():
    slow_function()
    optimized_fast_function()
    memory_intensive_function()


def profile_main():
    profiler = LineProfiler()
    profiler.add_function(slow_function)
    profiler.add_function(optimized_fast_function)
    profiler.add_function(memory_intensive_function)
    profiler.runcall(main)
    profiler.print_stats()


if __name__ == "__main__":
    profile_main()
