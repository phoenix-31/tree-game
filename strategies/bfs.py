from tree import Tree

def bfs(root: Tree, target_value) -> tuple[Tree, int]:
    cost = 0
    queue = [(root, 0)]  # (node, cumulative_cost)

    while queue:
        current_node, cumulative_cost = queue.pop(0)
        cost += cumulative_cost  # Add the cost to reach this node

        if current_node.value == target_value:
            return current_node, cost

        for edge_cost, child in current_node.get_children():
            queue.append((child, cumulative_cost + edge_cost))

    return None, cost
