import unittest
class ImmutableClass():

    def __init__(self, attrs={}):
        self.__dict__ = attrs

    ### immutable_class
    def __setattr__(self, name, value):
        raise Exception("Immutable Class can't be changed")
    ### end immutable_class 

class FunctionalToolsTest(unittest.TestCase):

    def test_list_comprehension(self):
        i_numbers = [ num for num in range(1,11) ] 

        self.assertEqual(len(i_numbers), 10)
        self.assertEqual(i_numbers[0], 1)
        self.assertEqual(i_numbers[9], 10)

    def test_map(self):
        i_numbers = [ num for num in range(1,11) ] 
        i_numbers = map(
                lambda i_num: i_num + 5}),
                i_numbers)

        self.assertEqual(len(i_numbers), 10)
        self.assertEqual(i_numbers[0].number , 6)
        self.assertEqual(i_numbers[9].number , 15)

    def test_filter(self):
        i_numbers = [ num for num in range(1,11) ] 
        i_numbers = filter(lambda num: num % 2, i_numbers)
        self.assertEqual(len(i_numbers), 5)

    def test_higher_order_functions(self):
        def converter(num):
            return ImmutableClass({"number":num.number + 2})

        i_numbers = [ ImmutableClass({"number":num}) for num in range(1,11) ] 

        new_numbers = map(converter, i_numbers)

        self.assertEqual(len(new_numbers), 10)
        self.assertEqual(new_numbers[0].number, 3)
        self.assertEqual(new_numbers[9].number, 12)

