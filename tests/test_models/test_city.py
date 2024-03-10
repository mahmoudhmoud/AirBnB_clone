#!/usr/bin/python3
'''
TESTS
'''
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    '''
    all tests are here
    '''

    def test_moduleDocs(self):
        '''
        testing
        '''
        moduleDoc = (
                __import__("models.city")
                .city.__doc__)
        self.assertGreater(len(moduleDoc), 0)

    def test_classDocs(self):
        '''
        testing
        '''
        classDoc = (
                __import__("models.city")
                .city.City.__doc__)
        self.assertGreater(len(classDoc), 0)

    def test_name_Type(self):
        '''
        testign
        '''
        city = City()
        self.assertIs(type(city.name), str)

    def test_state_id_Type(self):
        '''
        testing id type
        '''
        city = City()
        self.assertIs(type(city.state_id), str)


if __name__ == "__main__":
    unittest.main()
