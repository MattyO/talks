import unittest
import os
from os.path import dirname, join
import sys

sys.path.append(dirname(__file__))

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.contrib.auth.models import User
from django.test.simple import DjangoTestSuiteRunner

from myapp.models import Library, Book, Address

def load_fixture():
    the_place_to_be = Address.objects.create(street_address="THE place")

    our_library = Library.objects.create(name="our library", address=the_place_to_be)

    reader1 = User.objects.create_user(
            'me',
            'me@aol.com',
            'johnpassword')
    reader2 = User.objects.create_user(
            'you',
            'you@gmail.com',
            'johnpassword')
    john = User.objects.create_user(
            'jacob',
            'lennon@thebeatles.com',
            'johnpassword')
    jingleheimer = User.objects.create_user(
            'schmidt',
            'not@thebeatles.com',
            'johnpassword')

    a_tail = Book.objects.create(
            title="A Tale of Two Cities",
            author=john,
            location=our_library)

    a_tail.readers.add(reader1)
    a_tail.readers.add(reader2)

    a_tail.save()

    Book.objects.create(
            title="A Tale of One Cities",
            author=john,
            location=our_library)

    Book.objects.create(
            title="A Tale of no Cities",
            author=jingleheimer,
            location=our_library)

def model_to_dict(django_model, depth=1):
    temp_dict = {}
    for field in django_model._meta.local_fields:
        field_value = getattr(django_model, field.name)

        if isinstance(field, ForeignKey) and field_value is not None:
            if depth > 0:
                temp_dict[field.name] = model_to_dict(field_value, depth - 1)
        else:
            temp_dict[field.name] = field_value

    if depth > 0:
        for field in django_model._meta.local_many_to_many:
            field_list = []
            for m2m_item in getattr(django_model, field.name).all():
                field_list.append(model_to_dict(m2m_item, depth -1))
            temp_dict[field.name] = field_list

    return temp_dict

class ImmutableModel():
    def __init__(self, attrs={}):
        for key, value in attrs.items():
            if isinstance(value, list):
                attrs[key] = [ImmutableModel(da_hash) for da_hash in value]
            elif isinstance(value, dict):
                attrs[key] = ImmutableModel(value)

        self.__dict__ = attrs

    def __setattr__(self, name, value):
        raise Exception("Immutable Class can't be changed")


class ImmutableModelTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        test_runner = DjangoTestSuiteRunner(interactive=False, verbosity=1)
        test_db = test_runner.setup_databases()
        load_fixture()

        setattr(cls, "test_runner", test_runner)
        setattr(cls, "test_db", test_db)

    @classmethod
    def tearDownClass(cls):
        cls.test_runner.teardown_databases(cls.test_db)


    def test_converts_table_attributes(self):
        db_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        #db_user = User.objects.get(username='john')

        user = ImmutableModel(model_to_dict(db_user))

        self.assertEqual(user.username, "john")
        self.assertEqual(user.email, "lennon@thebeatles.com")
        self.assertNotEqual(user.password, "johnpassword")

    def test_is_immutable(self):
        db_user = User.objects.get(username='jacob')
        with self.assertRaises(Exception):
            user.username = "bill"

    def test_converts_relationships(self):
        book_hash = model_to_dict(Book.objects.get(title="A Tale of Two Cities"))
        i_book = ImmutableModel(book_hash)
        self.assertTrue(i_book.author.username, "jacob")

    def test_converts_many_to_many_relationships(self):
        book_hash = model_to_dict(Book.objects.get(title="A Tale of Two Cities"))
        i_book = ImmutableModel(book_hash)
        self.assertEqual(len(i_book.readers), 2)
        self.assertEqual(i_book.readers[0].username, "me")
        self.assertEqual(i_book.readers[1].username, "you")
