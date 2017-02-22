#! /usr/bin/env python
# -*-coding:utf-8 -*

__author__ = "Pascal LEFEVRE"
__copyright__ = ""
__credits__ = [__author__]
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = __author__
__email__ = "pascal.lefevre@univ-poitiers.fr"
__status__ = ""

import sys

from .context import example

def marker():
    # s = "<------------- actual test code\n"
    s = ""
    sys.stdout.write(s)

def setup_module(module):
    print("\nsetup_module      module:%s" % module.__name__)
 
def teardown_module(module):
    print("\nteardown_module   module:%s" % module.__name__)


def setup_function(function):
    print("\nsetup_function    function:%s" % function.__name__)

def teardown_function(function):
    print("\nteardown_function function:%s" % function.__name__)

# def test_1():
#     print('-  test_1()')
 
# def test_2():
#     print('-  test_2()')
 
 
# class TestClass:
 
#     @classmethod 
#     def setup_class(cls):
#         print ('\nsetup_class()')
 
#     @classmethod 
#     def teardown_class(cls):
#         print ('teardown_class()')
 
#     def setup_method(self, method):
#         print ('\nsetup_method()')
 
#     def teardown_method(self, method):
#         print ('\nteardown_method()')
 
#     def test_3(self):
#         print('- test_3()')
 
#     def test_4(self):
#         print('- test_4()')
    
def test_inc_3_4():
    assert example.inc(3) == 4
    marker()

def test_inc_3_5():
    assert example.inc(3) == 5
    marker()



def do():
    pass


def main():
    do()



if __name__ == '__main__':
    sys.exit(main())



