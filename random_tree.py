import random
from tree import Tree

def random_tree(max_depth, branching_factor, value_chooser, cost_chooser) -> Tree:
    if max_depth == 0:
        return Tree(value_chooser())

    root_value = value_chooser()
    root = Tree(root_value)

    if branching_factor > 0:
        num_children = random.randint(0, branching_factor)
        for _ in range(num_children):
            child_tree = random_tree(max_depth - 1, branching_factor, value_chooser, cost_chooser)
            cost = cost_chooser()
            root.add_child(cost, child_tree)

    return root
