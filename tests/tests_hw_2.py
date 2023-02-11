from HW_6_Tests.func_hw4 import create_folder
import unittest
from unittest import TestCase

token = ''
file_path = ''

class TestCheckFolder(TestCase):

    def test_check_success(self):
        res = create_folder(file_path, token)
        self.assertEqual(res.status_code, 200 or 201)

    @unittest.expectedFailure
    def test_check_error(self):
        res = create_folder(file_path, token)
        self.assertEqual(res.status_code, 404 or 409)


