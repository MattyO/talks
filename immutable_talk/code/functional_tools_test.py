import unittest

class ImmutableClass():
    def __init__(self, attrs={}):
        self.__dict__ = attrs

    def __setattr__(self, name, value):
        #temp_dict = self.__dict__
        #temp_dict[name] = value
        #self = ImmutableClass(temp_dict)
        raise Exception("Immutable Class can't be changed")

class FunctionalToolsTest(unittest.TestCase):

    def test_list_comprehension(self):
        i_numbers = [ ImmutableClass({"number":num}) for num in range(1,11) ] 
        self.assertEqual(len(i_numbers), 10)
        self.assertEqual(i_numbers[0].number, 1)
        self.assertEqual(i_numbers[9].number, 10)

    def test_map(self):
        i_numbers = [ ImmutableClass({"number":num}) for num in range(1,11) ] 
        i_numbers = map(lambda i_num:
                ImmutableClass({"number": i_num.number + 5}),
                i_numbers)

        self.assertEqual(len(i_numbers), 10)
        self.assertEqual(i_numbers[0].number , 6)
        self.assertEqual(i_numbers[9].number , 15)

    def test_filter(self):
        i_numbers = [ ImmutableClass({"number":num}) for num in range(1,11) ] 
        i_numbers = filter(lambda num: num.number % 2, i_numbers)
        self.assertEqual(len(i_numbers), 5)

    def test_higher_order_functions(self):
        def converter(num):
            return ImmutableClass({"number":num.number + 2})

        i_numbers = [ ImmutableClass({"number":num}) for num in range(1,11) ] 

        new_numbers = map(converter, i_numbers)

        self.assertEqual(len(new_numbers), 10)
        self.assertEqual(new_numbers[0].number, 3)
        self.assertEqual(new_numbers[9].number, 12)

