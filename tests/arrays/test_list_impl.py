__author__ = "Jieshu Wang and Bilal El Uneis"
__since__ = "July 2019"
__email__ = "foundwonder@gmail.com and bilaleluneis@gmail.com"

from unittest import TestCase
from data_structure.arrays.abstract import ArrayIndexOutOfBoundError
from data_structure.arrays.list_impl import ArrayListImpl
from typing import Optional
import logging as log


class TestArrayListImpl(TestCase):

    @classmethod
    def setUpClass(cls):
        log.basicConfig(level=log.INFO)

    def setUp(self):
        pass

    def test00_validate_instance_creation(self):
        test_array: ArrayListImpl = ArrayListImpl()
        self.assertTrue(test_array.size == 0)

    def test01_insert_without_index(self):
        test_array: ArrayListImpl = ArrayListImpl()
        test_array.insert(1)
        print_array = str(test_array)
        self.assertEqual('ArrayListImpl [1]', print_array)

    def test02_insert_with_index(self):
        test_array: ArrayListImpl = ArrayListImpl()
        test_array.insert(1)
        test_array.insert(5)
        for i in range(2, 5):
            test_array.insert(i, i - 1)
        print_array = str(test_array)
        self.assertEqual('ArrayListImpl [1, 2, 3, 4, 5]', print_array)

    def test03_insert_exception(self):
        test_array: ArrayListImpl = ArrayListImpl()  # empty
        test_array.insert(1)  # test_array = [1]
        test_array.insert(2)  # test_array = [1, 2]
        test_index_exception = [-1, 2, 5]
        for i in test_index_exception:
            with self.subTest(i):
                self.assertRaises(ArrayIndexOutOfBoundError, test_array.insert, 3, i)

    def test04_size_0(self):
        test_array_0 = self.__array_instance_generator()
        test_array_5 = self.__array_instance_generator(5)
        self.assertEqual(test_array_0.size, 0)
        self.assertEqual(test_array_5.size, 5)

    def test05_size_1(self):
        test_array = self.__array_instance_generator()
        for i in range(5):
            test_array.insert(i)
            with self.subTest(i):
                self.assertEqual(test_array.size, i + 1)

    def test06_get_happy_0(self):
        test_array = self.__array_instance_generator()
        for i in range(5):
            test_array.insert(i + 1)
            with self.subTest(i):
                self.assertEqual(test_array.get(i), i + 1)

    def test07_get_happy_1(self):
        test_array = self.__array_instance_generator(5)
        for i in range(5):
            with self.subTest(i):
                self.assertEqual(test_array.get(i), i + 1)

    def test08_get_none(self):
        test_array = self.__array_instance_generator()
        for i in range(5):
            test_array.insert(i + 1)
            with self.subTest(i):
                self.assertEqual(test_array.get(i + 2), None)
                self.assertEqual(test_array.get(-1), None)

    def test09_remove_return(self):
        test_array_0 = self.__array_instance_generator(5)
        test_array_1 = self.__array_instance_generator(5)
        self.assertEqual(test_array_0.remove(), 5)
        self.assertEqual(test_array_1.remove(3), 4)
        self.assertEqual(test_array_1.size, 4)

    def test10_remove_print(self):
        test_array = self.__array_instance_generator(5)
        test_array.remove(3)
        self.assertEqual('ArrayListImpl [1, 2, 3, 5]', str(test_array))

    def test11_remove_none(self):
        test_array = self.__array_instance_generator(4)
        invalid_index_list = [-1, 4, 9]
        for i in invalid_index_list:
            with self.subTest(i):
                self.assertEqual(None, test_array.remove(i))

    def test12_set_0(self):
        test_array = self.__array_instance_generator()
        for i in range(5):
            test_array.insert(i + 1)
        test_array.set(6, 3)
        self.assertEqual(test_array.get(3), 6)

    def test13_set_1(self):
        test_array = self.__array_instance_generator(5)
        for i in range(5):
            test_array.set(i + 10, i)
        for i in range(5):
            with self.subTest(i):
                test_value = test_array.get(i)
                self.assertEqual(test_value, i + 10)

    def test14_set_exception(self):
        test_array = self.__array_instance_generator(5)
        invalid_index_list = [-1, 5, 15]
        for i in invalid_index_list:
            with self.subTest(i):
                self.assertRaises(ArrayIndexOutOfBoundError, test_array.set, 6, i)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    """ Util Methods to Support Tests """

    def __array_instance_generator(self, size: Optional[int] = None) -> ArrayListImpl:
        if size is None or size == 0:
            self.array_instance: ArrayListImpl = ArrayListImpl()
        elif size > 0:
            self.array_instance: ArrayListImpl = ArrayListImpl()
            for i in range(size):
                self.array_instance.insert(i + 1)
        return self.array_instance
