from tree.tree import Tree

def dfs(root: Tree, target_value) -> tuple[Tree, int]:
    if root.value == target_value:
        return root, 0

    cost = 0
    for edge_cost, child in root.get_children():
        found_node, child_cost = dfs(child, target_value)
        cost += edge_cost + child_cost
        if found_node is not None:
            return found_node, cost
        
    return None, cost
