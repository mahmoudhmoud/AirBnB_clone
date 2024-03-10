#!/usr/bin/python3
'''
Tests
'''
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    '''
    all the test of Amenity class
    '''

    def test_moduleDocs(self):
        '''
        testing
        '''
        moduleDoc = (
                __import__("models.amenity")
                .amenity.__doc__)
        self.assertGreater(len(moduleDoc), 0)

    def test_classDocs(self):
        '''
        testing
        '''
        classDoc = (
                __import__("models.amenity")
                .amenity.Amenity.__doc__)
        self.assertGreater(len(classDoc), 0)

    def test_name_Type(self):
        '''
        testing the name
        '''
        amenity = Amenity()
        self.assertIs(type(amenity.name), str)


if __name__ == "__main__":
    unittest.main()
