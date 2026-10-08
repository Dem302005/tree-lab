"""7. Камери бінарного дерева (Binary Tree Cameras).

Жадібний алгоритм знизу вгору. Кожен вузол має один зі станів:
  0 — не покритий,  1 — на ньому стоїть камера,  2 — покритий без камери.
Порожній вузол вважаємо покритим (2). Для вузла:
  * якщо хоча б один нащадок не покритий (0) — ставимо камеру тут (стан 1);
  * інакше, якщо хоча б один нащадок має камеру (1) — вузол покритий (2);
  * інакше вузол не покритий (0) і чекає на батька.
Якщо корінь лишився не покритим — додаємо ще одну камеру.
Складність: O(n) за часом, O(h) за пам'яттю.
"""
from typing import Optional
from .tree_node import TreeNode

NOT_COVERED, HAS_CAMERA, COVERED = 0, 1, 2


def min_camera_cover(root: Optional[TreeNode]) -> int:
    cameras = 0
    state = {}
    stack = [(root, False)]
    while stack:
        node, visited = stack.pop()
        if node is None:
            continue
        if not visited:
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))
            continue
        left = state.get(node.left, COVERED)
        right = state.get(node.right, COVERED)
        if left == NOT_COVERED or right == NOT_COVERED:
            state[node] = HAS_CAMERA
            cameras += 1
        elif left == HAS_CAMERA or right == HAS_CAMERA:
            state[node] = COVERED
        else:
            state[node] = NOT_COVERED
    if root is not None and state[root] == NOT_COVERED:
        cameras += 1
    return cameras
