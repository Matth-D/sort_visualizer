def quicksort(input_array):
    if len(input_array) < 2:
        return input_array

    pivot = input_array[0]
    smaller = [i for i in input_array[1:] if i < pivot]
    greater = [i for i in input_array[1:] if i >= pivot]

    return quicksort(smaller) + [pivot] + quicksort(greater)


array = [1, 18, 91, 32, 1, 1, 9, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
print(quicksort(array))
