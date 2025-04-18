import unittest
from gen_bin_tree_rec_done import gen_bin_tree_rec_done

class TestRecursiveBinTreeGeneration(unittest.TestCase):
    def test_simple_case(self):
        expected = {'5': [{'25': []}, {'3': []}]}
        self.assertEqual(gen_bin_tree_rec_done(height=1), expected)

if __name__ == '__main__':
    unittest.main()