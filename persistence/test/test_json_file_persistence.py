__author__ = "Jieshu Wang and Bilal El Uneis"
__since__ = "Aug 2019"
__email__ = "foundwonder@gmail.com and bilaleluneis@gmail.com"

from unittest import TestCase
from persistence.abstract import AbstractPersistence
from persistence.file import JsonFilePersistence
from typing import Optional
from pathlib import Path


class TestJsonFilePersistence(TestCase):
    __persistence: Optional[AbstractPersistence] = None

    @classmethod
    def setUpClass(cls):
        if Path(str(Path.home()) + "/persistence.json").exists():
            Path(str(Path.home()) + "/persistence.json").unlink()

        if TestJsonFilePersistence.__persistence is None:
            TestJsonFilePersistence.__persistence = JsonFilePersistence()

    def test_1_persistence_empty(self):
        self.assertIsNone(TestJsonFilePersistence.__persistence.data)

    def test_2_persist_data(self):
        TestJsonFilePersistence.__persistence.data = {"name": "Bilal", "age": 90}
        self.assertIsNotNone(TestJsonFilePersistence.__persistence.data)
        if not all(key in TestJsonFilePersistence.__persistence.data for key in ["name", "age"]):
            self.fail()  # Fail only if not all the keys are found in the dictionary (__persistence.data)

    @classmethod
    def tearDownClass(cls):
        if Path(str(Path.home()) + "/persistence.json").exists():
            Path(str(Path.home()) + "/persistence.json").unlink()

        TestJsonFilePersistence.__persistence = None
