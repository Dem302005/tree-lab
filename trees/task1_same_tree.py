"""1. Те саме дерево (Same Tree).

Ідея: два дерева однакові, якщо їхні корені рівні, а ліві та праві піддерева
теж однакові. Порожні дерева (None) вважаються однаковими.
Складність: O(n) за часом, O(h) за пам'яттю (h — висота дерева).
"""
from typing import Optional
from .tree_node import TreeNode


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None and q is None:
        return True
    if p is None or q is None or p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
