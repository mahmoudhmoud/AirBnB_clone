#!/usr/bin/python3
'''
TESTS
'''
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    '''
    all tests
    '''

    def test_moduleDocs(self):
        '''
        testing
        '''
        moduleDoc = (
                __import__("models.user")
                .user.__doc__)
        self.assertGreater(len(moduleDoc), 0)

    def test_classDocs(self):
        '''
        testing
        '''
        classDoc = (
                __import__("models.user")
                .user.User.__doc__)
        self.assertGreater(len(classDoc), 0)

    def test_attributes_Type(self):
        '''
        testing
        '''
        user = User()
        self.assertIs(type(user.email), str)
        self.assertIs(type(user.password), str)
        self.assertIs(type(user.first_name), str)
        self.assertIs(type(user.last_name), str)


if __name__ == "__main__":
    unittest.main()
