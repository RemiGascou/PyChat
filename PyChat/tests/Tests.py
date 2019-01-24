# -*- coding: utf-8 -*-

from tests.testcases import *

class TestController(object):
    """docstring for TestController."""
    def __init__(self):
        super(TestController, self).__init__()
        self.s_test_passed = "\x1b[1m\x1b[92mPASSED\x1b[0m"
        self.s_test_failed = "\x1b[1m\x1b[91mFAILED\x1b[0m"

    def test(self, fname, f):
        maxlen = 65
        s = str("\x1b[1m[\x1b[93mTEST\x1b[0m\x1b[1m]\x1b[0m " + fname[:36]).ljust(maxlen, " ") + "... "
        print(s, end="")
        o = f()
        if o == True: print(self.s_test_passed)
        else : print(self.s_test_failed)


class Tests(object):
    """docstring for Tests."""
    def __init__(self):
        super(Tests, self).__init__()
        self.tc = TestController()

    def run_test(self):
        # Tests UI
        t = TestUI(self.tc)
        t.test()
