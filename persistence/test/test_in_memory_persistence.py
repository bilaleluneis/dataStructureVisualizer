__author__ = "Jieshu Wang and Bilal El Uneis"
__since__ = "Aug 2019"
__email__ = "foundwonder@gmail.com and bilaleluneis@gmail.com"

from unittest import TestCase
from persistence.abstract import AbstractPersistence
from persistence.memory import InMemoryPersistence
from typing import Optional


class TestInMemoryPersistance(TestCase):
    __persistence: Optional[AbstractPersistence] = None  # declared var of the Base Class Type

    @classmethod
    def setUpClass(cls):
        if TestInMemoryPersistance.__persistence is None:
            TestInMemoryPersistance.__persistence = InMemoryPersistence()

    def setUp(self):
        pass

    def test_1_persistance_is_empty(self):
        self.assertEqual(TestInMemoryPersistance.__persistence.data, None)

    def test_2_persist_data(self):
        TestInMemoryPersistance.__persistence.data = {"name": "Bilal", "age": 90}
        self.assertIsNotNone(TestInMemoryPersistance.__persistence.data)
        if not all(key in TestInMemoryPersistance.__persistence.data for key in ["name", "age"]):
            self.fail()  # Fail only if not all the keys are found in the dictionary (__persistence.data)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        TestInMemoryPersistance.__persistence = None
