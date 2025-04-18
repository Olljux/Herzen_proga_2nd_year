from gen_bin_tree_rec_done import gen_bin_tree_rec_done
from nonrec_gen_bin_tree_done import gen_bin_tree_nonrec
import matplotlib.pyplot as plt
import timeit
import random


def setup_data(n: int) -> list[tuple[int, int]]:
    data = []
    for _ in range(n):
        root = random.randint(1, 10)
        height = random.randint(1, 5)
        data.append((root, height))
    return data


def calculate_time(n: int, func) -> float:
    data = setup_data(n)
    total = 0
    for root, height in data:
        total += timeit.timeit(lambda: func(rt=root, height=height), number=1)
    return total / len(data)


def main():
    rec_times = []
    nonrec_times = []
    ns = range(10, 110, 10)

    for n in ns:
        rec_times.append(calculate_time(n, gen_bin_tree_rec_done))
        nonrec_times.append(calculate_time(n, gen_bin_tree_nonrec))

    plt.plot(ns, rec_times, label='Рекурсивная')
    plt.plot(ns, nonrec_times, label='Нерекурсивная')
    plt.xlabel("Количество запусков (n)")
    plt.ylabel("Среднее время выполнения (сек)")
    plt.title("Сравнение времени построения бинарного дерева")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()