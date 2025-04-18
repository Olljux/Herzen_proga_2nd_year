def gen_bin_tree_rec_done(rt=5, height=6, l_branch=lambda x: x**2, r_branch=lambda x: x - 2) -> dict:
    tree = {str(rt): []}
    if height == 0:
        return tree
    else:
        left_leaf = l_branch(rt)
        right_leaf = r_branch(rt)
        tree[str(rt)].append(gen_bin_tree_rec_done(rt=left_leaf, height=height - 1, l_branch=l_branch, r_branch=r_branch))
        tree[str(rt)].append(gen_bin_tree_rec_done(rt=right_leaf, height=height - 1,l_branch=l_branch, r_branch=r_branch))
    return tree


if __name__ == '__main__':
    import json
    tree = gen_bin_tree_rec_done()
    print(json.dumps(tree, indent=2))