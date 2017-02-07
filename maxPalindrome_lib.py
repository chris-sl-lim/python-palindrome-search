# -*- coding: utf-8 -*-
"""
maxPalindrome Library
Functions required by maxPalindrome.py (for retrieving unique palindromes)
Created on Sun Nov  6 10:15:10 2016

@author: Chris Lim
"""
def retrievePalindromesFromReducedSet(seq, palStore_reduced, palStore_original):
    """
    retrieves the actual palindromes from reduced palindromeStore list
    inputs:
        seq = original sequence string
        palStore_original = palindromeStore from maxPalindrome.py
        palStore_reduced = reduced palStore (suffixes/prefixes removes)
    outputs:
        maxPalindromes = strings containing maximum palindromes (sorted by descending length)
        maxPalStartIndex = start indices of maximum palindromes (sorted by descending length)
        maxPalLength = lengths of maximum palindromes (sorted by descending length)
    """
    # define stores
    maxPalStartIndex = []
    maxPalLength = []
    maxPalindromes = []

    # look for centers (designated by -2) and get surrounding chars
    maxIndex = [i for i, j in enumerate(palStore_reduced) if j == -2]
    for i in range(0, len(maxIndex)):
        currentMaxCenter = maxIndex[i]
        currentMaxLength = palStore_original[maxIndex[i]]

        if not(currentMaxCenter % 2):
            # center is between two characters
            centerChar = int(currentMaxCenter/2)
            startChar = int(centerChar - currentMaxLength/2)
            endChar = int(startChar + currentMaxLength)
            maxPalindrome = seq[startChar:endChar]
        else:
            # center is on a character
            centerChar = int(currentMaxCenter/2)
            startChar = int(centerChar - (currentMaxLength-1)/2)
            endChar = int(startChar + currentMaxLength)
            maxPalindrome = seq[startChar:endChar]
        
        #add to stores    
        maxPalStartIndex.append(startChar)
        maxPalLength.append(currentMaxLength)
        maxPalindromes.append(maxPalindrome)
        
    # sort in descending order using zip method
    sortedMaxPalindromes = list(zip(maxPalLength, maxPalStartIndex, maxPalindromes))
    sortedMaxPalindromes.sort(reverse=True)
    
    # unzip sorted lists
    maxPalLength = [x for x, y, z in sortedMaxPalindromes]
    maxPalStartIndex = [y for x, y, z in sortedMaxPalindromes]
    maxPalindromes = [z for x, y, z in sortedMaxPalindromes]
        
    return maxPalindromes, maxPalStartIndex, maxPalLength 
        
    
    
    
def findNLargestUniquePalindromes(palStore_original, N):
    """
    finds the N largest unique palindromes in the palindromeStore using the
    findLargestUniquePalindrome method
    inputs:
        palStore_original = palindromeStore from maxPalindrome.py
        N = number of palindromes requested
    outputs:
        palStore = edited palindromeStore with suffixes/prefixes removed for N largest
    """
    
    from maxPalindrome_lib import findLargestUniquePalindrome
    
    # create copy of original to avoid destroying it
    palStore = palStore_original.copy()
    
    print('\n-------------------------------------------------')
    print('finding largest unique palindromes by reduction')
    
    for i in range(0, N):
        # check that there are still positive values to pick that are non-
        # singular.
        palStore_set = set(palStore)
        if len([x for x in palStore_set if x > 1]) > 0:
            # if there are still valid values, reduce palStore again
            print('reducing palindromeStore,  step {0}'.format(i))
            palStore = findLargestUniquePalindrome(palStore)
        else:
            # if there aren't, break out of loop
            print('no more unique palindromes ({0}/{1} found)'.format(i, N))
            break
        
    # end of for loop should yield reduced palStore
    return palStore
    
    


def findLargestUniquePalindrome(palStore_original):
    """
    finds the largest unique palindrome and removes the suffixes and prefixes
    inputs:
        palStore_original = palindromeStore from maxPalindrome.py
    outputs:
        palStore = edited palindromeStore with suffixes/prefixes removed
    """
    # create copy of original to avoid destroying it
    palStore = palStore_original.copy()
    
    # get first occurance of max value in palindromeStore
    maxIndex = palStore.index(max(palStore))
    maxPalLength = palStore[maxIndex]

    # loop ahead and behind maxIndex to remove suffixes and prefixes
    # put center as -2 and anything that would be suffix/prefix as -1
    startIndex = maxIndex - maxPalLength + 1
    endIndex = maxIndex + maxPalLength - 1
    for j in range(startIndex, endIndex):
        if j == maxIndex:
            palStore[j] = -2
        else:
            palStore[j] = -1

    return palStore
