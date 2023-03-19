import unittest
from unittest.mock import patch
from io import StringIO
from algo import getter_links, evaluate, heuristic, evaluate_using_heuristic
import unittest

class TestWikiGame(unittest.TestCase):
    def test_evaluate_simple(self):
        expected = "['Mango', 'Apple']"
        result = evaluate('Mango', 'Apple')
        self.assertEqual(expected, result)

    def test_evaluate_using_heuristic_simple(self):
        expected = "['Mango', 'Apple']"
        result = evaluate_using_heuristic('Mango', 'Apple')
        self.assertEqual(expected, result)

    def test_evaluate_invalid_input(self):
        expected = None
        result = evaluate('hfsiuebgfuwgvius', 'afuerfqjbackuieri')
        self.assertEqual(expected, result)

    def test_evaluate_using_heuristic_invalid_input(self):
        expected = None
        result = evaluate_using_heuristic('afeuirgbfhjcugsfe', 'afuyy3trfsgurf')
        self.assertEqual(expected, result)

    def test_evaluate_same_word(self):
        expected = ['Mango']
        result = evaluate('Mango', 'Mango')
        self.assertEqual(expected, result)

    def test_evaluate_using_heuristic_same_word(self):
        expected = ['Mango']
        result = evaluate_using_heuristic('Mango', 'Mango')
        self.assertEqual(expected, result)

    def test_evaluate_using_heuristic_shortest_path(self):
        expected = "['Mango', 'Apple']"
        result = evaluate_using_heuristic('Mango', 'Apple')
        self.assertEqual(expected, result)

test = TestWikiGame()
#if test passes then print "Test passed"
print("Testing evaluate_simple()...")
if(test.test_evaluate_same_word() == None):
    print("Test passed")
else:
    print("Test failed")
# print("Testing evaluate_complex()...")
# if(test.test_evaluate_complex()==None):
#     print("Test passed")
# else:
#     print("Test failed")
print("Testing evaluate_using_heuristic_simple()...")
if(test.test_evaluate_using_heuristic_simple()==None):
    print("Test passed")
else:
    print("Test failed")
print("Testing evaluate_invalid_input()...")
if(test.test_evaluate_invalid_input()==None):
    print("Test passed")
else:
    print("Test failed")
print("Testing evaluate_using_heuristic_invalid_input()...")
if(test.test_evaluate_using_heuristic_invalid_input()==None):
    print("Test passed")
else:
    print("Test failed")
print("Testing evaluate_same_word()...")
if(test.test_evaluate_same_word()==None):
    print("Test passed")
else :
    print("Test failed")
print("Testing evaluate_using_heuristic_same_word()...")
if(test.test_evaluate_using_heuristic_same_word()==None):
    print("Test passed")
else:
    print("Test failed")
print("Testing evaluate_using_heuristic_shortest_path()...")
if(test.test_evaluate_using_heuristic_shortest_path()==None):
    print("Test passed")
else:
    print("Test failed")

