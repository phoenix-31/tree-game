import heapq
from tree import Tree

def ucs(root: Tree, target_value) -> tuple[Tree, int]:
    queue = [(0, root)]  # (cost, node)

    while queue:
        current_cost, current_node = heapq.heappop(queue)

        if current_node.value == target_value:
            return current_node, current_cost

        for cost, child in current_node.get_children():
            heapq.heappush(queue, (current_cost + cost, child))

    return None, current_cost
