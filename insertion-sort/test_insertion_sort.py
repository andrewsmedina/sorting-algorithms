from insertion_sort import insertion_sort

import unittest


class InsertionSortTestCase(unittest.TestCase):

    def test_insertion_sort_should_sort_a_list(self):
        self.assertEqual([1, 2, 3, 4, 5], insertion_sort([4, 2, 3, 5, 1]))


unittest.main()
