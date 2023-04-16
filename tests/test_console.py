#!/usr/bin/python3
"""This is unittest for the console module"""
import sys
import unittest
import os
from console import HBNBCommand
from models.__init__ import storage
sys.path.append('../')


class TestConsole(unittest.TestCase):
    """Test class for HBNBCommand class"""

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_quit(self):
        pass

    def test_EOF(self):
        pass

    def test_create(self):
        arg = 'State name="California"'
        self.console.do_create(arg)
        storage.reload()
        self.assertTrue(os.path.exists('./file.json'), True)

if __name__ == '__main__':
    unittest.main()
