"""6. Двійкове дерево: максимальна сума шляху (Binary Tree Maximum Path Sum).

Ідея: для кожного вузла рахуємо "внесок" — найбільшу суму шляху, що йде від
вузла вниз в один бік (від'ємні гілки відкидаємо, беручи max(.., 0)).
Шлях, у якому цей вузол є вершиною: val + внесок_лівий + внесок_правий.
Відповідь — максимум за всіма вузлами. Обхід post-order ітеративний
(глибина дерева може сягати 30 000).
Складність: O(n) за часом, O(h) за пам'яттю.
"""
from typing import Optional
from .tree_node import TreeNode


def max_path_sum(root: Optional[TreeNode]) -> int:
    best = float("-inf")
    gain = {}                       # вузол -> найкращий внесок вниз
    stack = [(root, False)]
    while stack:
        node, visited = stack.pop()
        if node is None:
            continue
        if not visited:
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))
        else:
            left = max(gain.get(node.left, 0), 0)
            right = max(gain.get(node.right, 0), 0)
            best = max(best, node.val + left + right)
            gain[node] = node.val + max(left, right)
    return best
