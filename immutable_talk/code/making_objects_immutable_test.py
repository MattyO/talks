import unittest
class ImmutableClass():
    def __init__(self, attrs={}):
        self.__dict__ = attrs

    def __setattr__(self, name, value):
        raise Exception("Immutable Class can't be changed")

class ImmutableTest(unittest.TestCase):

    def test_can_make_with_attrs(self):
        class_attributes = {"thing_one":"value one", "thing_two":"value two"}
        my_instance = ImmutableClass(class_attributes)

        self.assertIsInstance(my_instance, ImmutableClass)

    def test_can_get_attributes(self):
        my_instance = ImmutableClass({"thing_one":"value one", "thing_two":"value two"})

        self.assertEqual(my_instance.thing_one, "value one")
        self.assertEqual(my_instance.thing_two, "value two")

    def test_cant_change_attributes(self):
        my_instance = ImmutableClass({"thing_one":"value one", "thing_two":"value two"})

        with self.assertRaises(Exception) as ex:
            my_instance.thing_one = "some other value"


