import unittest


def addem(x, y):
    """
    This function adds two numbers together.
    :param x: Number 1.
    :param y: Number 2.
    :return: Number 1 plus Number 2.
    :example: addem(1,2) -> 3
    """
    raise NotImplementedError("Finish me! Delete this line and code.")


class TestAddEm(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(addem(1, 2), 3)
        self.assertEqual(addem(2, 3), 5)

    def test_nonwhole(self):
        self.assertEqual(addem(0.5, 0.5), 1)
        self.assertEqual(addem(1, 0.5), 1.5)

    def test_nested(self):
        self.assertEqual(addem(addem(1, 2), 3), 6)
        self.assertEqual(addem(addem(1, 2), 0.3), 3.3)
