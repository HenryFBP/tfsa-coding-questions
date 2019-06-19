import unittest


def addem(x, y):
    """
    This function adds two numbers together.
    :param x: Number 1.
    :param y: Number 2.
    :return: Number 1 plus Number 2.
    :example: addem(1,2) -> 3
    """
    raise NotImplementedError("Finish me!")


class TestAddEm(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(addem(1, 2), 3)
