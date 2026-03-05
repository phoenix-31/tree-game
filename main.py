import random
from random_tree import random_tree
from strategies.bfs import bfs
from strategies.ucs import ucs
from strategies.dfs import dfs

def main():
    value_chooser = lambda: random.randbytes(4).hex()  # Generate random hex string as value
    cost_chooser = lambda: random.randint(1, 10)
    tree = random_tree(8, 3, value_chooser, cost_chooser)

    target_value = random.choice([node.value for node in tree])
    print(f"Searching for value: {target_value}")

    bfs_result, bfs_cost = bfs(tree, target_value)
    print(f"BFS found: {bfs_result.value if bfs_result else None}, cost: {bfs_cost}")

    ucs_result, ucs_cost = ucs(tree, target_value)
    print(f"UCS found: {ucs_result.value if ucs_result else None}, cost: {ucs_cost}")

    dfs_result, dfs_cost = dfs(tree, target_value)
    print(f"DFS found: {dfs_result.value if dfs_result else None}, cost: {dfs_cost}")


if __name__ == "__main__":
    main()
