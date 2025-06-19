def two_sum_hashed_all(lst, target):
    seen = {}
    used_indices = set()
    result = []

    for index, value in enumerate(lst):
        needed = target - value
        if needed in seen:
            i = seen[needed]
            j = index
            if i not in used_indices and j not in used_indices:
                pair = (i, j) if i < j else (j, i)
                result.append(pair)
                used_indices.add(i)
                used_indices.add(j)
        if value not in seen:
            seen[value] = index

    result.sort()
    return result

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 8
result = two_sum_hashed_all(lst, target)
print(result)