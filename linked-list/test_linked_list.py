import unittest

from linked_list import LinkedList


class LinkedListTestCase(unittest.TestCase):

    def test_linked_list(self):
        ll = LinkedList()
        for i in range(10):
            ll.add(i)
        self.assertEqual(list(range(10)), ll.list())


unittest.main()
