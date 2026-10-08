"""2. Симетричне дерево (Symmetric Tree).

Ідея: порівнюємо пари вузлів, які мають бути дзеркальними: ліве піддерево
одного з правим піддеревом іншого. Реалізовано ітеративно (стек пар),
щоб не залежати від ліміту рекурсії.
Складність: O(n) за часом, O(h) за пам'яттю.
"""
from typing import Optional
from .tree_node import TreeNode


def is_symmetric(root: Optional[TreeNode]) -> bool:
    if root is None:
        return True
    stack = [(root.left, root.right)]
    while stack:
        a, b = stack.pop()
        if a is None and b is None:
            continue
        if a is None or b is None or a.val != b.val:
            return False
        stack.append((a.left, b.right))
        stack.append((a.right, b.left))
    return True
