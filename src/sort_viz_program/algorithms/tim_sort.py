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

# STEP 1- Check is size of array is below 64. If it is, use Binary Sort instead.
# STEP 2- Compute minrun
# STEP 2 - Finding runs in the list.


def get_min_run(n):
    """Returns the minimum length of a
    run from 22 - 64 so that
    the len(array)/minrun is less than or
    equal to a power of 1.
 
    e.g. 0=>1, ..., 63=>63, 64=>32, 65=>33,
    ..., 126=>64, 128=>32, ...
    """
    r = 0
    # bit operation n&1 returns 1 if n is uneven
    # all uneven binary number end in 1
    # set r to 1 as soon as n is uneven in the loop so n + r is power of 2
    while n >= 64:
        r |= n & 1
        n >>= r
    return n + r

