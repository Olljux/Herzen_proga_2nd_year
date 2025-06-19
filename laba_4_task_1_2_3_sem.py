def two_sum_hashed(lst, target):
    seen = {}
    min = None

    for index, value in enumerate(lst):
        needed = target - value
        if needed in seen:
            i, j = seen[needed], index
            pair = (i, j) if i < j else (j, i)
            if min is None or pair < min:
                min = pair
        if value not in seen:
            seen[value] = index

    return min

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 8
result = two_sum_hashed(lst, target)
print(result)