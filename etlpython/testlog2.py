#!/usr/bin/env python
# -*- coding: utf-8 -*-

import testlog,sys

@testlog.runpylog('testpython.log')
def testlog(args):
    print 'log test2 succ'
    return 'test 2 succ'

if __name__ == '__main__':
    st=testlog(sys.argv)
    print st