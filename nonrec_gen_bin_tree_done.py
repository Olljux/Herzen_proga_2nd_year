def gen_bin_tree_nonrec(rt=5, height=6, l_branch=lambda x: x * x, r_branch=lambda x: x - 2) -> dict:
    roots = [[rt]]


    for lesf in range(height):
        if len(roots) == 1:
            r = roots[0]
        else:
            r = [item for s in roots[-1] for item in s]

        leaves = list(map(lambda rt_value: [l_branch(rt_value), r_branch(rt_value)], r))
        roots.append(leaves)

    roots.reverse()
    roots[-1] = [roots[-1]]
    roots[0] = list(map(lambda x: [{str(x[0]): []},{str(x[1]): []}], roots[0]))

    print(f"roots, {roots}")

    for i in range(height):
        sublist = roots[i]
        print(f"sublist > {sublist}")
        for j in range(len(sublist)):
            x = sublist.pop()
            roots[i + 1][j // 2][j % 2] = {str(roots[i + 1][j // 2][j % 2]): x}
    print(f"roots, {roots}")

    tree = roots[-1][0][0]
    return tree


if __name__ == '__main__':
    print(gen_bin_tree_nonrec(rt=5, height=3))