"""3. Інвертувати бінарне дерево (Invert Binary Tree).

Ідея: у кожному вузлі міняємо місцями лівого та правого нащадка.
Складність: O(n) за часом, O(h) за пам'яттю.
"""
from typing import Optional
from .tree_node import TreeNode


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    stack = [root]
    while stack:
        node = stack.pop()
        if node is None:
            continue
        node.left, node.right = node.right, node.left
        stack.append(node.left)
        stack.append(node.right)
    return root
