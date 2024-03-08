#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.mod = BaseModel()
    def tearDown(self):
        print("___")

    def test_init(self):
        self.assertIsNotNone(self.mod.id)
        self.assertIsNotNone(self.mod.created_at)
        self.assertIsNotNone(self.mod.updated_at)

    def test_save(self):
        pv = self.mod.updated_at
        cr = self.mod.save()
        self.assertNotEqual(pv, cr)

    def test_to_dic(self):

        self.assertIsNotNone(self.mod.__dict__)
        self.assertIsNotNone(self.mod.__class__.__name__)
        self.assertIsNotNone(self.mod.created_at.isoformat())
        self.assertIsNotNone(self.mod.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
