
def bubble_sort(a):
    for _ in range(len(a)):
        for c in range(len(a) - 1):
            if a[c] > a[c + 1]:
                a[c], a[c + 1] = a[c + 1], a[c]
                yield a.copy()


my_array = [27, 45, 89, 12, 3, 67, 54, 76, 34, 90, 8, 23, 56, 78, 91, 14, 68, 29, 50, 95]
for i, step in enumerate(bubble_sort(my_array), 1):
    print(f"Step {i}: {step}")