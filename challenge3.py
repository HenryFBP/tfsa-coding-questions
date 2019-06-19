import unittest


def followDirections(directions):
    """
    Given a string comprised of four characters, '^', 'v', '<', and '>', return an (x,y) tuple that
    represents following those directions on a taxicab-distance grid.

    You start at (0, 0) and the coordinates are (x, y).

    :example: followDirections("") -> (0, 0)
    :example: followDirections("v") -> (0, -1)
    :example: followDirections(">>>^") -> (3, 1)
    :example: followDirections(">v<^") -> (0, 0)

    """
    raise NotImplementedError("Finish me! Delete this line and code.")


class TestCats(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(followDirections(""), 0)
