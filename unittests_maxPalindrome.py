# -*- coding: utf-8 -*-
"""
Maximal palindrome search - unit tests
Created on Mon Nov  7 10:15:10 2016

@author: Chris Lim
"""

#import modules
import unittest
from maxPalindrome import findMaximumPalindromes

class DictionaryDashTestCases(unittest.TestCase):
    """Tests for `dictionary_dash.main()`."""
    # preparing to test
    def setUp(self):
        """ Setting up for the test """
        print('---------------------------------------------\n')
        print('STARTING TEST...')

    def test_Request3PalindromeFail(self):
        print('Request 3 palindromes, but pass argument with only 1 unique')
        seq = 'abbacabba'
        noOfPalindromes = 3
        self.assertFalse(len(findMaximumPalindromes(seq, noOfPalindromes)) == 3)
        
    def test_Request1PalindromePass(self):
        print('Request 1 palindromes, but pass argument with only 1 unique')
        seq = 'abababa'
        noOfPalindromes = 1
        self.assertTrue(len(findMaximumPalindromes(seq, noOfPalindromes)) == 1)
        
    def test_PassOriginalSequence(self):
        print('Pass original sequence')
        seq = 'sqrrqabccbatudefggfedvwhijkllkjihxymnnmzpop'
        noOfPalindromes = 3
        self.assertTrue(len(findMaximumPalindromes(seq, noOfPalindromes)) == 3)
        
    def test_UpperCaseNumerics(self):
        print('Pass upper case and numerical characters')
        seq = 'HYTBCABADEFGHABCDEDCBAGHTFYW1234567887654321ZWETYGDE'
        noOfPalindromes = 1
        self.assertTrue(len(findMaximumPalindromes(seq, noOfPalindromes)) == 1)   
        
    def test_Reques5Palindromes(self):
        print('Request 5 palindromes')
        seq = 'abc12321DEF45654ghi78987jkl24642mno97579pqr'
        noOfPalindromes = 5
        self.assertTrue(len(findMaximumPalindromes(seq, noOfPalindromes)) == 5)

    def test_Request3Largest(self):
        print('Pass upper case and numerical characters')
        seq = 'abc12321DEF12345654321ghi6789876jkl112464211mno97579pqr'
        noOfPalindromes = 3
        self.assertTrue(len(findMaximumPalindromes(seq, noOfPalindromes)) == 3)    
        
    def test_PalindromeBetweenChar(self):
        print('Check it detects palindromes existing around centers between chars')
        seq = 'abba'
        noOfPalindromes = 1
        self.assertTrue(len(findMaximumPalindromes(seq, noOfPalindromes)) == 1) 
        
    def test_PalindromeBetweenChar2(self):
        print('Check it detects palindromes existing around centers between chars')
        seq = 'abba456AABBBBAA789101987'
        noOfPalindromes = 3
        self.assertTrue(len(findMaximumPalindromes(seq, noOfPalindromes)) == 3)  
        
    def test_AdjacentPalindromes(self):
        print('Pass argument with palindromes adjacent to one another')
        seq = 'abbaghjklkjhg12345678987654321'
        noOfPalindromes = 3
        self.assertTrue(len(findMaximumPalindromes(seq, noOfPalindromes)) == 3)   
        
    def test_NoPalindromes(self):
        print('Pass argument with no palindromes')
        seq = 'abcdefghijklmnopqrstuvwxyz'
        noOfPalindromes = 3
        self.assertTrue(len(findMaximumPalindromes(seq, noOfPalindromes)) == 0)

    def test_OverlappingPalindromes(self):
        print('Pass argument with overlapping palindromes')
        seq = 'abdeffedbaaaaaabba'
        noOfPalindromes = 3
        self.assertTrue(len(findMaximumPalindromes(seq, noOfPalindromes)) == 3)

    def test_RecurringPalindromes(self):
        print('Pass argument with recurring palindromes')
        seq = 'dgadggffggsdfjshjshjsggffgglkgfjdf'
        noOfPalindromes = 2
        self.assertTrue(len(findMaximumPalindromes(seq, noOfPalindromes)) == 2)                          

if __name__ == '__main__':
    unittest.main()