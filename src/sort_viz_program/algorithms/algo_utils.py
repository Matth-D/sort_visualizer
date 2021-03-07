import re
import numpy as np


def is_subarray(slice, superset):
    """Check if input slice is subset of second input.

    Args:
        slice (np.array): Slice numpy array.
        superset (np.array): Array superset.

    Returns:
        [bool]: Returns True if first input subset of second input, False if not.
    """
    slice_str = np.array2string(slice)
    slice_str = re.sub(r"[\[\]]", "", slice_str)

    superset_str = np.array2string(superset)
    superset_str = re.sub(r"[\[\]]", "", superset_str)

    return slice_str in superset_str
