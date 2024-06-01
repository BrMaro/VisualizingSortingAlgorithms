import random

#return true if sorted
def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def bogo_sort(a):
    while not is_sorted(a):
        random.shuffle(a)
        yield a.copy()
#
# my_array = [27, 45, 89, 12, 3, 67, 54, 76, 34, 90, 8, 23, 56, 78, 91, 14, 68, 29, 50, 95]
# for i, step in enumerate(bogo_sort(my_array), 1):
#     print(f"Step {i}: {step}")