"""9. Відновити дерево після попереднього обходу (Recover a Tree From Preorder).

Ідея: читаємо рядок зліва направо. Спочатку рахуємо тире — це глибина D,
потім читаємо число. Тримаємо стек поточного шляху від кореня:
  * видаляємо зі стека вузли, поки його розмір більше D —
    на вершині опиниться батько нового вузла;
  * якщо в батька ще немає лівого нащадка — це лівий, інакше правий
    (за умовою єдиний нащадок завжди лівий);
  * кладемо новий вузол у стек.
Складність: O(n) за часом і пам'яттю.
"""
from typing import Optional
from .tree_node import TreeNode


def recover_from_preorder(traversal: str) -> Optional[TreeNode]:
    stack = []
    i, n = 0, len(traversal)
    while i < n:
        depth = 0
        while i < n and traversal[i] == "-":
            depth += 1
            i += 1
        start = i
        while i < n and traversal[i].isdigit():
            i += 1
        node = TreeNode(int(traversal[start:i]))

        while len(stack) > depth:
            stack.pop()
        if stack:
            parent = stack[-1]
            if parent.left is None:
                parent.left = node
            else:
                parent.right = node
        stack.append(node)
    return stack[0] if stack else None
