import random
from random_tree import random_tree
from bfs import bfs
from ucs import ucs
from dfs import dfs

def main():
    tree = random_tree(10, 5)  # max_value=10, max_children=5

    target_value = random.choice(range(1, 11))
    print(f"Searching for value: {target_value}")

    bfs_result, bfs_cost = bfs(tree, target_value)
    print(f"BFS found: {bfs_result.value if bfs_result else None}, cost: {bfs_cost}")

    ucs_result, ucs_cost = ucs(tree, target_value)
    print(f"UCS found: {ucs_result.value if ucs_result else None}, cost: {ucs_cost}")

    dfs_result, dfs_cost = dfs(tree, target_value)
    print(f"DFS found: {dfs_result.value if dfs_result else None}, cost: {dfs_cost}")


if __name__ == "__main__":
    main()
