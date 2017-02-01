#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

'''
Run tests in simple form:
python2 ./ml.py test
'''

import sys
import unittest

import save_http_page

def fetch_robots():
    dst_address = 'https://medium.com/robots.txt'
    file_name = 'm.html'
    save_http_page.save_page_to_file(dst_address, file_name)

class TestML(unittest.TestCase):
    '''
    General class for testing
    '''
    def test_ml(self):
        '''
        TestML:
        '''
        self.assertEqual(0, 1)

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'test':
        unittest.main(argv=sys.argv[:1])
    else:
        fetch_robots()
