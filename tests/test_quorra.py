#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# testing for coda
# 
# @author <bprinty@gmail.com>
# ------------------------------------------------


# imporobj
# -------
import unittest
import os
import subprocess

import quorra
from . import __base__


# session
# -------
class TestEntryPoints(unittest.TestCase):

    def call(self, subcommand, *args):
        return subprocess.check_output('python -m quorra {} {}'.format(
            subcommand, ' '.join(args)
        ), stderr=subprocess.STDOUT, shell=True, cwd=__base__)

    def test_version(self):
        res = self.call('version')
        self.assertTrue(res, quorra.__version__)
        return


# exec
# ----
if __name__ == '__main__':
    unittest.main()
