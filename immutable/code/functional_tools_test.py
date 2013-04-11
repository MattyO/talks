import unittest
### immutable_class
class ImmutableClass():

    def __init__(self, attrs={}):
        self.__dict__ = attrs

    ### immutable_method
    def __setattr__(self, name, value):
        raise Exception("Immutable Class can't be changed")
    ### end immutable_method
### end immutable_class

class FunctionalToolsTest(unittest.TestCase):

    def test_list_comprehension(self):
        ### list_comprehension
        i_numbers = [ num + 2 for num in range(1,11) ] 
        ### end list_comprehension

        self.assertEqual(len(i_numbers), 10)
        self.assertEqual(i_numbers[0], 3)
        self.assertEqual(i_numbers[9], 12)

    def test_map(self):
        ### map
        some_numbers = range(1,11)
        some_numbers = map( lambda a_number: a_number + 5, some_numbers )
        ### end map

        self.assertEqual(len(some_numbers), 10)
        self.assertEqual(some_numbers[0], 6)
        self.assertEqual(some_numbers[9], 15)

    def test_filter(self):

        ### filter
        i_numbers = range(1,11)
        i_numbers = filter(lambda num: num % 2, i_numbers)
        ### end filter

        self.assertEqual(len(i_numbers), 5)

    def test_higher_order_functions(self):
        ### higher_functions
        def converter(num):
            return ImmutableClass({"number":num.number + 2})

        i_numbers = [ ImmutableClass({"number":num}) for num in range(1,11) ] 

        new_numbers = map(converter, i_numbers)
        ### end higher_functions

        self.assertEqual(len(new_numbers), 10)
        self.assertEqual(new_numbers[0].number, 3)
        self.assertEqual(new_numbers[9].number, 12)

