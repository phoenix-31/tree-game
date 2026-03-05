class Tree:
    def __init__(self, value: int):
        self.value = value
        self.children = []

    def add_child(self, cost: int, child_node: "Tree"):
        self.children.append((cost, child_node))

    def get_children(self):
        return self.children

    def __lt__(self, other):
        return self.value < other.value

    def __repr__(self):
        return f"Tree(value={self.value}, children={len(self.children)})"
