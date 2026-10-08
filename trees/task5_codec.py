"""5. Серіалізація та десеріалізація бінарного дерева (Serialize/Deserialize).

Формат: обхід по рівнях (BFS), значення розділені комою, відсутній вузол
позначається символом '#'. Приклад: "1,2,3,#,#,4,5".
Усе робиться ітеративно, тому дерево глибиною 10 000 не ламає рекурсію.
Складність: O(n) за часом і пам'яттю.
"""
from collections import deque
from typing import Optional
from .tree_node import TreeNode


def serialize(root: Optional[TreeNode]) -> str:
    if root is None:
        return ""
    parts = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            parts.append("#")
        else:
            parts.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
    return ",".join(parts)


def deserialize(data: str) -> Optional[TreeNode]:
    if not data:
        return None
    tokens = data.split(",")
    root = TreeNode(int(tokens[0]))
    queue = deque([root])
    i = 1
    while queue and i < len(tokens):
        node = queue.popleft()
        if tokens[i] != "#":
            node.left = TreeNode(int(tokens[i]))
            queue.append(node.left)
        i += 1
        if i < len(tokens) and tokens[i] != "#":
            node.right = TreeNode(int(tokens[i]))
            queue.append(node.right)
        i += 1
    return root


class Codec:
    """Обгортка у стилі LeetCode."""

    def serialize(self, root: Optional[TreeNode]) -> str:
        return serialize(root)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        return deserialize(data)
