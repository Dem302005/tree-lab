"""4. K-й найменший елемент у BST (Kth Smallest Element in a BST).

Ідея: симетричний (inorder) обхід BST видає значення у зростаючому порядку,
тому зупиняємось на k-му вузлі. Обхід ітеративний, через стек.
Складність: O(h + k) за часом, O(h) за пам'яттю.
"""
from typing import Optional
from .tree_node import TreeNode


def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    stack = []
    node = root
    while stack or node:
        while node:                 # йдемо максимально вліво
            stack.append(node)
            node = node.left
        node = stack.pop()
        k -= 1
        if k == 0:
            return node.val
        node = node.right
    raise ValueError("k більше за кількість вузлів у дереві")
