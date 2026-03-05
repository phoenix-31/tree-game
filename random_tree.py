import random
from tree import Tree

def random_tree(max_value, max_children) -> Tree:
    if max_value <= 0:
        return None

    value = random.randint(1, max_value)
    cost = random.randint(1, 10)  # Random cost for the edge to this node
    num_children = random.randint(0, max_children)
    children = [random_tree(max_value, max_children - 1) for _ in range(num_children)]
    tree = Tree(value)
    for child in children:
        if child is not None:
            tree.add_child(cost, child)
    return tree
