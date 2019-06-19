import unittest


def howManyCats(string):
    """
    Given a string, return how many times the word "cat" appears, case-sensitive.
    :example: howManyCats("catcat") -> 2
    :example: howManyCats("catCat") -> 1
    :example: howManyCats("atact") -> 0
    """
    raise NotImplementedError("Finish me! Delete this line and code.")


class TestCats(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(howManyCats(""), 0)
        self.assertEqual(howManyCats("cat"), 1)
        self.assertEqual(howManyCats("cattcacat"), 2)
        self.assertEqual(howManyCats("cCat"), 0)

    def test_long(self):
        self.assertEqual(howManyCats("cat" * 9999), 9999)
        self.assertEqual(howManyCats("cat" * 99999), 99999)
