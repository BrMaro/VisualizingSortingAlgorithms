def merge_sort(a, step=1):
    if len(a) > 1:
        left_a = a[:len(a) // 2]
        right_a = a[len(a) // 2:]

        # recursively divide the arrays and yield intermediate steps
        yield from merge_sort(left_a, step=step+1)
        yield from merge_sort(right_a, step=step+1)

        i = 0
        j = 0
        k = 0

        while i < len(left_a) and j < len(right_a):
            if left_a[i] < right_a[j]:
                a[k] = left_a[i]
                i += 1
            else:
                a[k] = right_a[j]
                j += 1
            k += 1
            yield step, a  # yield the step number and the current state of the array

        while i < len(left_a):
            a[k] = left_a[i]
            i += 1
            k += 1
            yield step, a  # yield the step number and the current state of the array

        while j < len(right_a):
            a[k] = right_a[j]
            j += 1
            k += 1
            yield step, a  # yield the step number and the current state of the array

my_array = [27, 45, 89, 12, 3, 67, 54, 76, 34, 90, 8, 23, 56, 78, 91, 14, 68, 29, 50, 95]
print(merge_sort(my_array))
for i, step in enumerate(merge_sort(my_array), 1):
    print(f"Step {i}: {step}")
