#!/usr/bin/python3
'''
TESTS
'''
import unittest
from models.state import State


class TestState(unittest.TestCase):
    '''
    all tests
    '''

    def test_moduleDocs(self):
        '''
        testing
        '''
        moduleDoc = (
                __import__("models.state")
                .state.__doc__)
        self.assertGreater(len(moduleDoc), 0)

    def test_classDocs(self):
        '''
        testing
        '''
        classDoc = (
                __import__("models.state")
                .state.State.__doc__)
        self.assertGreater(len(classDoc), 0)

    def test_name_Type(self):
        '''
        testing
        '''
        state = State()
        self.assertIs(type(state.name), str)


if __name__ == "__main__":
    unittest.main()
