__author__ = "Bilal El Uneis & Jieshu Wang"
__since__ = "Jul 2019"
__email__ = "bilaleluneis@gmail.com, foundwonder@gmail.com"

from unittest import TestCase
from arrays.stack_object import Stack
from arrays.list_impl import ArrayListImpl
from arrays.node_impl import ArrayNodeImpl
import logging as log


class TestStack(TestCase):
    __stack_list_impl: Stack = Stack(ArrayListImpl())
    __stack_node_impl: Stack = Stack(ArrayNodeImpl())

    @classmethod
    def setUpClass(cls):
        log.basicConfig(level=log.INFO)

    def setUp(self):
        pass

    def test00_validate_instance_creation(self):
        self.assertTrue(TestStack.__stack_list_impl.size == 0)
        self.assertTrue(TestStack.__stack_node_impl.size == 0)
        self.assertEqual('Stack []', str(TestStack.__stack_list_impl))
        self.assertEqual('Stack []', str(TestStack.__stack_node_impl))

    def test01_pop_empty(self):
        test_stack_list_impl = TestStack.__stack_list_impl
        test_stack_node_impl = TestStack.__stack_node_impl
        popped_value_list_impl = test_stack_list_impl.pop()
        popped_value_node_impl = test_stack_node_impl.pop()
        self.assertEqual(popped_value_list_impl, None)
        self.assertEqual(popped_value_node_impl, None)
        self.assertEqual(test_stack_list_impl.size, 0)
        self.assertEqual(test_stack_node_impl.size, 0)
        self.assertEqual('Stack []', str(test_stack_list_impl))
        self.assertEqual('Stack []', str(test_stack_node_impl))

    def test02_push_empty(self):
        test_stack_list_impl = TestStack.__stack_list_impl
        test_stack_node_impl = TestStack.__stack_node_impl
        test_stack_list_impl.push(1)
        test_stack_node_impl.push(1)
        self.assertEqual('Stack [1]', str(test_stack_list_impl))
        self.assertEqual('Stack [1]', str(test_stack_node_impl))

    def test03_push_non_empty(self):
        test_stack_list_impl = TestStack.__stack_list_impl
        test_stack_node_impl = TestStack.__stack_node_impl
        test_stack_list_impl.push(2)
        test_stack_node_impl.push(2)
        self.assertEqual('Stack [1, 2]', str(test_stack_list_impl))
        self.assertEqual('Stack [1, 2]', str(test_stack_node_impl))

    def test04_pop_non_empty(self):
        test_stack_list_impl = TestStack.__stack_list_impl
        test_stack_node_impl = TestStack.__stack_node_impl
        popped_value_list_impl = test_stack_list_impl.pop()
        popped_value_node_impl = test_stack_node_impl.pop()
        self.assertEqual(popped_value_list_impl, 2)
        self.assertEqual(popped_value_node_impl, 2)
        self.assertEqual(test_stack_list_impl.size, 1)
        self.assertEqual(test_stack_node_impl.size, 1)
        self.assertEqual('Stack [1]', str(test_stack_list_impl))
        self.assertEqual('Stack [1]', str(test_stack_node_impl))

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass
