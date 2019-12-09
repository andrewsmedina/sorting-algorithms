import unittest
from quickunion import QuickUnion


class QuickUnionTestCase(unittest.TestCase):
    def test_quick_union(self):
        qf = QuickUnion()
       
        result = qf.add(3, 4)
        self.assertFalse(result)

        result = qf.add(4, 9)
        self.assertFalse(result)

        result = qf.add(8, 0)
        self.assertFalse(result)

        result = qf.add(2, 3)
        self.assertFalse(result)

        result = qf.add(5, 6)
        self.assertFalse(result)

        result = qf.add(2, 9)
        self.assertTrue(result)

        result = qf.add(2, 4)
        self.assertTrue(result)


unittest.main()
