from heap_sort import heap_sort

import unittest


class HeapSortTestCase(unittest.TestCase):

    def test_heap_sort_should_sort_a_list(self):
        self.assertEqual([1, 2, 3, 4, 5], heap_sort([4, 2, 3, 5, 1]))


unittest.main()
