__author__ = "Jieshu Wang and Bilal El Uneis"
__since__ = "July 2019"
__email__ = "foundwonder@gmail.com and bilaleluneis@gmail.com"

from unittest import TestCase
import logging as log
from data_structure.arrays.node_impl import *


class TestArrayNodeImpl(TestCase):

    __node_array: ArrayNodeImpl = ArrayNodeImpl()

    @classmethod
    def setUpClass(cls) -> None:
        log.basicConfig(level=log.INFO)

    def setUp(self) -> None:
        pass

    def test01_instance_creation(self):
        self.assertTrue(self.__node_array.size == 0)
        self.assertEqual('ArrayNodeImpl []', str(self.__node_array))

    def test02_insert_without_index(self):
        test_array = self.__node_array
        for i in range(3):
            with self.subTest(i):
                test_array.insert(5 - i)
                self.assertEqual(test_array.size, i+1)
        self.assertEqual('ArrayNodeImpl [5, 4, 3]', str(test_array))

    def test03_get_happy(self):
        test_array = self.__node_array
        for i in range(3):
            with self.subTest(i):
                self.assertEqual(test_array.get(i), 5 - i)

    def test04_get_none(self):
        test_array = self.__node_array
        test_index = (-1, 5, 13)
        for i in test_index:
            with self.subTest(i):
                self.assertEqual(test_array.get(i), None)
        test_array_0: ArrayNodeImpl = ArrayNodeImpl()
        self.assertEqual(test_array_0.get(0), None)

    def test05_insert_with_index(self):
        test_array = self.__node_array
        for i in range(3):
            with self.subTest(i):
                test_array.insert(9 - i, i)
                self.assertEqual(test_array.size, 4+i)
        self.assertEqual('ArrayNodeImpl [9, 8, 7, 5, 4, 3]', str(test_array))

    def test06_insert_without_index_2(self):
        test_array = self.__node_array
        test_array.insert(2)
        self.assertEqual(test_array.size, 7)
        self.assertEqual('ArrayNodeImpl [9, 8, 7, 5, 4, 3, 2]', str(test_array))

    def test07_insert_exception(self):
        test_array = self.__node_array
        test_index_exception = [-1, 8, 15]
        for i in test_index_exception:
            with self.subTest(i):
                self.assertRaises(ArrayIndexOutOfBoundError, test_array.insert, 3, i)

    def test08_remove_without_index(self):
        test_array = self.__node_array
        result = test_array.remove()
        self.assertEqual(result, 2)
        self.assertEqual(test_array.size, 6)
        self.assertEqual('ArrayNodeImpl [9, 8, 7, 5, 4, 3]', str(test_array))

    def test09_remove_without_index_from_empty_array(self):
        test_array = ArrayNodeImpl()
        result = test_array.remove()
        self.assertEqual(result, None)
        self.assertEqual(test_array.size, 0)
        self.assertEqual('ArrayNodeImpl []', str(test_array))

    def test10_remove_with_index(self):
        test_array = self.__node_array
        result = test_array.remove(0)
        self.assertEqual(result, 9)
        self.assertEqual(test_array.size, 5)
        self.assertEqual('ArrayNodeImpl [8, 7, 5, 4, 3]', str(test_array))

    def test11_remove_with_index_empty(self):
        test_array = ArrayNodeImpl()
        test_array.insert(1)
        result = test_array.remove(5)
        self.assertEqual(result, None)
        self.assertEqual(test_array.size, 1)
        self.assertEqual('ArrayNodeImpl [1]', str(test_array))

    def test12_insert_with_index_empty(self):
        test_array = ArrayNodeImpl()
        test_array.insert(5, 0)
        self.assertEqual(test_array.size, 1)
        self.assertEqual('ArrayNodeImpl [5]', str(test_array))

    def test_set_happy(self):
        test_array = self.__node_array
        test_array.set(10, 0)
        self.assertEqual(test_array.get(0), 10)
        self.assertEqual('ArrayNodeImpl [10, 7, 5, 4, 3]', str(test_array))

    def test_set_out_of_bound(self):
        test_array = self.__node_array
        test_array.set(10, 200)
        self.assertEqual(test_array.get(200), None)
        self.assertEqual(test_array.size, 5)

    def tearDown(self) -> None:
        self.array = None

    @classmethod
    def tearDownClass(cls) -> None:
        pass
