# -----------------------------------------------------------------------------
#                     The CodeChecker Infrastructure
#   This file is distributed under the University of Illinois Open Source
#   License. See LICENSE.TXT for details.
# -----------------------------------------------------------------------------
"""
File reading tests.
"""
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import os
import unittest

from libcodechecker.util import get_line


class GetLineTest(unittest.TestCase):
    """
    Tests to get source file lines.
    """

    def test_util_getline(self):
        """
        Lines in files with carriage return character
        should be handled as separate lines.
        """
        test_file_path = os.path.dirname(os.path.realpath(__file__))
        file_to_process = os.path.join(test_file_path, 'newline')

        line1 = get_line(file_to_process, 1)
        self.assertEqual(line1, 'line1\n')

        line2 = get_line(file_to_process, 2)
        self.assertEqual(line2, 'line2\n')

        line4 = get_line(file_to_process, 4)
        self.assertEqual(line4, 'line4\n')

        line5 = get_line(file_to_process, 5)
        self.assertEqual(line5, 'line5\n')

        line6 = get_line(file_to_process, 6)
        self.assertEqual(line6, 'line6\n')
