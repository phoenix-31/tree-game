from typing import TypeVar, Generator

T = TypeVar('T')

class Tree[T]:
    def __init__(self, value: T):
        self.value = value
        self.children = []

    def get_children(self) -> list[tuple[int, "Tree[T]"]]:
        return self.children

    def add_child(self, cost: int, child_node: "Tree[T]"):
        self.children.append((cost, child_node))

    def __lt__(self, other: "Tree[T]") -> bool:
        return self.value < other.value
    
    def __iter__(self) -> Generator["Tree[T]", None, None]:
        yield self
        for _, child in self.children:
            yield from child

    def __repr__(self) -> str:
        return f"Tree(value={self.value}, children={len(self.children)})"
