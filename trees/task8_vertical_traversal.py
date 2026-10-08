"""8. Вертикальний обхід бінарного дерева (Vertical Order Traversal).

Ідея: обходимо дерево й для кожного вузла запам'ятовуємо (стовпець, рядок,
значення). Лівий нащадок має (рядок+1, стовпець-1), правий — (рядок+1,
стовпець+1). Потім сортуємо трійки: спочатку за стовпцем, далі за рядком
(зверху вниз), далі за значенням — і групуємо за стовпцями.
Складність: O(n log n) за часом, O(n) за пам'яттю.
"""
from collections import defaultdict
from typing import List, Optional
from .tree_node import TreeNode


def vertical_traversal(root: Optional[TreeNode]) -> List[List[int]]:
    if root is None:
        return []
    items = []
    stack = [(root, 0, 0)]          # (вузол, рядок, стовпець)
    while stack:
        node, row, col = stack.pop()
        items.append((col, row, node.val))
        if node.left:
            stack.append((node.left, row + 1, col - 1))
        if node.right:
            stack.append((node.right, row + 1, col + 1))
    items.sort()
    columns = defaultdict(list)
    for col, _, val in items:
        columns[col].append(val)
    return [columns[c] for c in sorted(columns)]
