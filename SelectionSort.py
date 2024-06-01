# runs selection sort but makes a change for every run of the game loop not at once
def selection_sort(a):
    n = len(a)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j

        a[i], a[min_index] = a[min_index], a[i]
        yield a.copy()


# my_array = [27, 45, 89, 12, 3, 67, 54, 76, 34, 90, 8, 23, 56, 78, 91, 14, 68, 29, 50, 95]
# for i, step in enumerate(selection_sort(my_array), 1):
#     print(f"Step {i}: {step}")
