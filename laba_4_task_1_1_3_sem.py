def two_sum(lst, target):
    min = None
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:
                if min is None or (i, j) < min:
                    min = (i, j)

    return min

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 8
result = two_sum(lst, target)
print(result)