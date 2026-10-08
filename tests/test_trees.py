"""Тести: усі приклади з умови + кілька додаткових (граничних) випадків.
Запуск з кореня репозиторію:  python -m unittest -v
"""
import unittest

from trees.tree_node import TreeNode, build_tree, to_list
from trees.task1_same_tree import is_same_tree
from trees.task2_symmetric_tree import is_symmetric
from trees.task3_invert_tree import invert_tree
from trees.task4_kth_smallest import kth_smallest
from trees.task5_codec import Codec, serialize, deserialize
from trees.task6_max_path_sum import max_path_sum
from trees.task7_binary_tree_cameras import min_camera_cover
from trees.task8_vertical_traversal import vertical_traversal
from trees.task9_recover_from_preorder import recover_from_preorder

N = None


class TestSameTree(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(is_same_tree(build_tree([1, 2, 3]), build_tree([1, 2, 3])))
        self.assertFalse(is_same_tree(build_tree([1, 2]), build_tree([1, N, 2])))
        self.assertFalse(is_same_tree(build_tree([1, 2, 1]), build_tree([1, 1, 2])))

    def test_empty(self):
        self.assertTrue(is_same_tree(None, None))
        self.assertFalse(is_same_tree(None, build_tree([1])))


class TestSymmetric(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(is_symmetric(build_tree([1, 2, 2, 3, 4, 4, 3])))
        self.assertFalse(is_symmetric(build_tree([1, 2, 2, N, 3, N, 3])))

    def test_edge(self):
        self.assertTrue(is_symmetric(None))
        self.assertTrue(is_symmetric(build_tree([1])))
        self.assertFalse(is_symmetric(build_tree([1, 2, 3])))


class TestInvert(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(to_list(invert_tree(build_tree([4, 2, 7, 1, 3, 6, 9]))),
                         [4, 7, 2, 9, 6, 3, 1])
        self.assertEqual(to_list(invert_tree(build_tree([2, 1, 3]))), [2, 3, 1])
        self.assertEqual(to_list(invert_tree(build_tree([]))), [])


class TestKthSmallest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(kth_smallest(build_tree([3, 1, 4, N, 2]), 1), 1)
        self.assertEqual(kth_smallest(build_tree([5, 3, 6, 2, 4, N, N, 1]), 3), 3)

    def test_last(self):
        self.assertEqual(kth_smallest(build_tree([5, 3, 6, 2, 4, N, N, 1]), 6), 6)


class TestCodec(unittest.TestCase):
    def roundtrip(self, values):
        codec = Codec()
        return to_list(codec.deserialize(codec.serialize(build_tree(values))))

    def test_examples(self):
        self.assertEqual(self.roundtrip([1, 2, 3, N, N, 4, 5]), [1, 2, 3, N, N, 4, 5])
        self.assertEqual(self.roundtrip([]), [])

    def test_negative_and_single(self):
        self.assertEqual(self.roundtrip([-1000, 1000, N, -5]), [-1000, 1000, N, -5])
        self.assertEqual(self.roundtrip([7]), [7])

    def test_format(self):
        self.assertEqual(serialize(build_tree([1, 2, 3, N, N, 4, 5])), "1,2,3,#,#,4,5,#,#,#,#")
        self.assertIsNone(deserialize(""))

    def test_deep_tree_no_recursion_error(self):
        root = TreeNode(0)
        node = root
        for i in range(1, 10000):          # вироджене дерево з 10 000 вузлів
            node.right = TreeNode(i)
            node = node.right
        restored = deserialize(serialize(root))
        count = 0
        while restored:
            count += 1
            restored = restored.right
        self.assertEqual(count, 10000)


class TestMaxPathSum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_path_sum(build_tree([1, 2, 3])), 6)
        self.assertEqual(max_path_sum(build_tree([-10, 9, 20, N, N, 15, 7])), 42)

    def test_negative(self):
        self.assertEqual(max_path_sum(build_tree([-3])), -3)
        self.assertEqual(max_path_sum(build_tree([-2, -1])), -1)

    def test_deep(self):
        root = TreeNode(1)
        node = root
        for _ in range(29999):
            node.left = TreeNode(1)
            node = node.left
        self.assertEqual(max_path_sum(root), 30000)


class TestCameras(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(min_camera_cover(build_tree([0, 0, N, 0, 0])), 1)
        self.assertEqual(min_camera_cover(build_tree([0, 0, N, 0, N, 0, N, N, 0])), 2)

    def test_edge(self):
        self.assertEqual(min_camera_cover(build_tree([0])), 1)
        self.assertEqual(min_camera_cover(build_tree([0, 0, 0])), 1)


class TestVertical(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(vertical_traversal(build_tree([3, 9, 20, N, N, 15, 7])),
                         [[9], [3, 15], [20], [7]])
        self.assertEqual(vertical_traversal(build_tree([1, 2, 3, 4, 5, 6, 7])),
                         [[4], [2], [1, 5, 6], [3], [7]])
        self.assertEqual(vertical_traversal(build_tree([1, 2, 3, 4, 6, 5, 7])),
                         [[4], [2], [1, 5, 6], [3], [7]])

    def test_single(self):
        self.assertEqual(vertical_traversal(build_tree([1])), [[1]])


class TestRecoverFromPreorder(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(to_list(recover_from_preorder("1-2--3--4-5--6--7")),
                         [1, 2, 5, 3, 4, 6, 7])
        self.assertEqual(to_list(recover_from_preorder("1-2--3---4-5--6---7")),
                         [1, 2, 5, 3, N, 6, N, 4, N, 7])
        self.assertEqual(to_list(recover_from_preorder("1-401--349---90--88")),
                         [1, 401, N, 349, 88, 90])

    def test_single_and_big_value(self):
        self.assertEqual(to_list(recover_from_preorder("1000000000")), [1000000000])


if __name__ == "__main__":
    unittest.main()
