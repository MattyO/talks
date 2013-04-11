import unittest

### add-two
def f(x):
    return x + 2
### end add-two

class SimpleTest(unittest.TestCase):
    def test_f_plus_2(self):
        self.assertEqual( f(2), 4)

    def test_f_plus_4(self):
        self.assertEqual( f(4), 6 )

