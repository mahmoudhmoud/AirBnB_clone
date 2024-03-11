#!/usr/bin/python3
"""
Module to test
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.mod = BaseModel()

    def tearDown(self):
        print("----")

    def test_init(self):
        self.assertIsNotNone(self.mod.id)
        self.assertIsNotNone(self.mod.created_at)
        self.assertIsNotNone(self.mod.updated_at)

    def test_save(self):
        pv_updated = self.mod.updated_at
        cr_updated = self.mod.save()
        self.assertNotEqual(pv_updated, cr_updated)

    def test_to_dict(self):
        dic = self.mod.to_dict()
        self.assertIsNotNone(dic["__class__"])
        self.assertIsNotNone(dic["id"])
        self.assertIsNotNone(dic["created_at"])
        self.assertIsNotNone(dic["updated_at"])
        self.assertEqual(dic["__class__"], "BaseModel")
        self.assertEqual(dic["id"], self.mod.id)
        self.assertEqual(dic["created_at"], self.mod.created_at.isoformat())
        self.assertEqual(dic["updated_at"], self.mod.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
