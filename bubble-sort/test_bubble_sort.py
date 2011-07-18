from bubble_sort import bubble_sort

import unittest


class BubbleSortTestCase(unittest.TestCase):

    def test_bubble_sort_should_sort_a_list(self):
        self.assertEqual([1, 2, 3, 4, 5], bubble_sort([4, 2, 3, 5, 1]))


unittest.main()
