#!/usr/bin/python3
'''
TESTS
'''
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    '''
    testing
    '''

    def test_moduleDocs(self):
        '''
        testing
        '''
        moduleDoc = (
                __import__("models.review")
                .review.__doc__)
        self.assertGreater(len(moduleDoc), 0)

    def test_classDocs(self):
        '''
        testing
        '''
        classDoc = (
                __import__("models.review")
                .review.Review.__doc__)
        self.assertGreater(len(classDoc), 0)

    def test_attributes_Type(self):
        '''
        testing
        '''
        review = Review()
        self.assertIs(type(review.text), str)
        self.assertIs(type(review.place_id), str)
        self.assertIs(type(review.user_id), str)


if __name__ == "__main__":
    unittest.main()
