from pathlib import Path
import sys
sys.path.append(str(Path(sys.path[0]).parent))

from extract_inner_function import extract_inner_function
import unittest

class TestMain(unittest.TestCase):

    def test_extract_inner_function__simple(self):
        def outer():
            def inner1():
                return "from_inner1"
            def inner2():
                return
        func = extract_inner_function(outer, "inner1")
        self.assertEqual(func(), "from_inner1")

    def test_extract_inner_function__with_args(self):
        def outer(a, b):
            def inner1(a, b, c):
                return a + b + c
            def inner2(a, b):
                return
        func = extract_inner_function(outer, "inner1")
        self.assertEqual(func(4, 5, 6), 15)

    def test_extract_inner_function__multiple_nests(self):
        def outer():
            def inner1():
                def inner2():
                    def inner3():
                        return "from inner3"
            def inner4():
                return
        func = extract_inner_function(outer, "inner3")
        self.assertEqual(func(), "from inner3")

if __name__ == "__main__":
    unittest.main()
