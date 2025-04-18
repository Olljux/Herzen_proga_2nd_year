import timeit
import matplotlib.pyplot as plt
from random import randint


# Рекурсивная генерация бинарного дерева
def gen_bin_tree_rec_done(rt=5, height=6, l_branch=lambda x: x ** 2, r_branch=lambda x: x - 2) -> dict:
    tree = {str(rt): []}
    if height == 0:
        return tree
    else:
        left_leaf = l_branch(rt)
        right_leaf = r_branch(rt)
        tree[str(rt)].append(
            gen_bin_tree_rec_done(rt=left_leaf, height=height - 1, l_branch=l_branch, r_branch=r_branch))
        tree[str(rt)].append(
            gen_bin_tree_rec_done(rt=right_leaf, height=height - 1, l_branch=l_branch, r_branch=r_branch))
    return tree


# Нерекурсивная генерация бинарного дерева
def gen_bin_tree_nonrec(rt=5, height=6, l_branch=lambda x: x * x, r_branch=lambda x: x - 2) -> dict:
    roots = [[rt]]

    for _ in range(height):
        if len(roots) == 1:
            r = roots[0]
        else:
            r = [item for s in roots[-1] for item in s]

        leaves = list(map(lambda rt_value: [l_branch(rt_value), r_branch(rt_value)], r))
        roots.append(leaves)

    roots.reverse()
    roots[-1] = [roots[-1]]
    roots[0] = list(map(lambda x: [{str(x[0]): []}, {str(x[1]): []}], roots[0]))

    for i in range(height):
        sublist = roots[i]
        for j in range(len(sublist)):
            x = sublist.pop()
            roots[i + 1][j // 2][j % 2] = {str(roots[i + 1][j // 2][j % 2]): x}

    tree = roots[-1][0][0]
    return tree


# Генерация случайных данных для тестов
def setup_data(n: int) -> list:
    data = []
    for _ in range(n):
        root = randint(1, 100)
        height = randint(1, 10)
        data.append((root, height))
    return data


# Замер времени выполнения
def calculate_time(n: int, func) -> float:
    data = setup_data(n)
    delta = 0
    for root, height in data:
        start_time = timeit.default_timer()
        func(rt=root, height=height)
        delta += timeit.default_timer() - start_time
    return delta


# Построение графиков
def main():
    res_rec = []
    res_nonrec = []
    for n in range(10, 100, 10):
        res_rec.append(calculate_time(n, gen_bin_tree_rec_done))
        res_nonrec.append(calculate_time(n, gen_bin_tree_nonrec))

    plt.plot(range(10, 100, 10), res_rec, label="Рекурсивная")
    plt.plot(range(10, 100, 10), res_nonrec, label="Нерекурсивная")
    plt.xlabel('Число замеров (n)')
    plt.ylabel('Время (с.)')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()