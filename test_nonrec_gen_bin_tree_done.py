import unittest
from nonrec_gen_bin_tree_done import gen_bin_tree_nonrec

class TestNonRecursiveBinTreeGeneration(unittest.TestCase):
    def test_simple_case(self):
        self.assertEqual(gen_bin_tree_nonrec(rt=5, height=1), {'5': [{'25': []}, {'3': []}]})