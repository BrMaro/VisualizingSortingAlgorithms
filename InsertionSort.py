def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key
        yield a.copy()

#
# my_array = [27, 45, 89, 12, 3, 67, 54, 76, 34, 90, 8, 23, 56, 78, 91, 14, 68, 29, 50, 95]
# for i, step in enumerate(insertion_sort(my_array), 1):
#     print(f"Step {i}: {step}")