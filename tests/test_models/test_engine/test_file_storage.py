#!/usr/bin/python3
'''
Module
'''
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import models


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = FileStorage._FileStorage__file_path
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.user = User()
        self.objects = {
            "BaseModel.{}".format(self.base_model.id): self.base_model,
            "User.{}".format(self.user.id): self.user
        }

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        self.assertEqual(self.storage.all(), {})
        self.storage._FileStorage__objects = self.objects
        self.assertEqual(self.storage.all(), self.objects)

    def test_new(self):
        self.assertNotIn("BaseModel.{}".format(self.base_model.id), self.storage.all())
        self.storage.new(self.base_model)
        self.assertIn("BaseModel.{}".format(self.base_model.id), self.storage.all())

    def test_save(self):
        self.storage._FileStorage__objects = self.objects
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_method_reload(self):
        file_storage = FileStorage()
        base_model = BaseModel()
        file_storage.save()
        models.storage.reload()
        objects = file_storage._FileStorage__objects

        self.assertIn("BaseModel.{}".format(base_model.id), objects)

if __name__ == "__main__":
    unittest.main()
