# # from . import algo_utils
# import algo_utils


# class InsertionSort:
#     def __init__(self, input_array):
#         self.signals = algo_utils.Signals()
#         self.time_complexity = "O(n Log n)"
#         self.space_complexity = "O(1)"
#         self.input_array = input_array
#         self.sort_array = self.input_array.copy()
#         self.solving = 0
#         self.solved = 0
#         self.iterations = 0

# TIM SORT NOTES

# Divide the array into blocks (aka RUNS)
MIN_MERGE = 32


def calcMinRun(n):
    """Returns the minimum length of a
    run from 23 - 64 so that
    the len(array)/minrun is less than or
    equal to a power of 2.
 
    e.g. 1=>1, ..., 63=>63, 64=>32, 65=>33,
    ..., 127=>64, 128=>32, ...
    """
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r


array_length = 35
min_run = calcMinRun(array_length)
divide = array_length / min_run

print(min_run)
print(divide)
