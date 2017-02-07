# -*- coding: utf-8 -*-
"""
Maximal palindrome search (based on Jeuring algorithm, 2004)
Main function: findMaximumPalindromes (logs to findMaximumPalindromes.log)
    inputs:
        sequence = original sequence to search
        noOfPalindromes = number of palindromes requested
    outputs:
        maxPalindromes = strings containing maximum palindromes (sorted by descending length)
Created on Sun Nov  6 10:15:10 2016

@author: Chris Lim
"""
def findMaximumPalindromes(sequence, noOfPalindromes):
    
    from maxPalindrome_lib import findNLargestUniquePalindromes
    from maxPalindrome_lib import retrievePalindromesFromReducedSet
    from timeit import default_timer as timer
    import logging

    # set logger settings
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    
    # create a file handler for logger
    handler = logging.FileHandler('findMaximumPalindromes.log')
    handler.setLevel(logging.INFO)
    
    # add the handlers to the logger
    logger.addHandler(handler)
    
    # start timer
    startTime = timer()
    
    # variables and data stores
    sequenceLength = len(sequence)
    palindromeStore = []
    palindromeLength = 0
    currentPos = 0
    
    # start search
    print('\nPALINDROME SEARCH')
    print('sequence: {0}'.format(sequence))
    
    # start the loop
    while currentPos < sequenceLength:
        
        # step summary
        logger.info('----------------------------------')
        logger.info('current position: {0} out of {1} characters' \
                  .format(currentPos, sequenceLength-1))
        logger.info('current palindromeLength: {0}'.format(palindromeLength))
        logger.info('current position: {0}[{1}]{2}'.format(sequence[0:currentPos], \
              sequence[currentPos], sequence[currentPos+1:]))
        logger.info('current palindromeStore: {0}'.format(palindromeStore))
            
        # find center (if even, then center is between two characters)
        currentCenter = len(palindromeStore)/2
        if not(currentCenter % 1):
            currentCenter = int(currentCenter)
            logger.info('current center: {0}[]{1}'.format(sequence[0:currentCenter], \
                  sequence[currentCenter:]))
        else:
            currentCenter = int(currentCenter)
            logger.info('current center: {0}[{1}]{2}'.format(sequence[0:currentCenter], \
                  sequence[currentCenter],sequence[currentCenter+1:]))
                
        # look to extend current palindrome
        if currentPos > palindromeLength and \
            sequence[currentPos - palindromeLength - 1] == sequence[currentPos]:
            
            logger.info('extending palindrome...')
            palindromeLength += 2
            currentPos += 1
            
            # jumps back to top of while loop and ends step
            continue
        
        # when this loop finishes, palindrome is as long as it'll get so store it
        logger.info('cannot extend palindrome, commence prefix search...')
        palindromeStore.append(palindromeLength)
        
        # look for centre of palindrome suffix
        # start from second to last of current center (previous character) up to
        # edge of last palindrome
        lookbackStart = len(palindromeStore) - 2
        lookbackEnd = lookbackStart - palindromeLength
        
        logger.info('looking for prefix from from {0} to {1}'.format(lookbackStart, lookbackEnd))    
            
        for i in range(lookbackStart, lookbackEnd, -1):
            # set criterion for left edge detection (prefix) and loop back
            prefixCriterion = i - lookbackEnd - 1
            if palindromeStore[i] == prefixCriterion:
                logger.info('prefix found at index {0} in palindromeStore'.format(i))
                palindromeLength = prefixCriterion           
                # breaks out of for loop
                break
            
            else:
                # otherwise copy value over to the right side if suffix not found
                # append min value to avoid palindromes extending past edge
                logger.info('prefix not found, copying center index {0} to RHS'.format(i))
                palindromeStore.append(min(prefixCriterion, palindromeStore[i]))       
        else:
            # if palindromeLength is 0 (ie first step) or prefix isn't found, then
            # consider palindrome around currentPos
            logger.info('prefix not found, consider palindrome around current center')
            palindromeLength = 1
            currentPos += 1
            
    # end of while loop
    
    # reached end of the word, append last palindrome
    logger.info('\n-------------------------------------------------')
    logger.info('reached the end of the word, extend palindrome store if not full')
    palindromeStore.append(palindromeLength)
    
    # now, if we have to, fill in the rest of palinedromeStore
    palindromeStoreLength = len(palindromeStore)
    palStoreExpectedLength = 2 * sequenceLength + 1
    
    lookbackStart = palindromeStoreLength - 2
    lookbackEnd = lookbackStart - (palStoreExpectedLength - palindromeStoreLength)
    for i in range(lookbackStart, lookbackEnd, -1):
        endCheck = i - lookbackEnd - 1
        palindromeStore.append(min(endCheck, palindromeStore[i]))
        logger.info('extending palindromeStore: {0}'.format(palindromeStore))
    
    # display final palindromeStore
    logger.info('Final Palindrome Store: {0}'.format(palindromeStore))
    
    # now we have palinedromes, check for unique palindromes
    palStore_reduced = findNLargestUniquePalindromes (palindromeStore, noOfPalindromes)
    
    # retrieve palindromes from reduced set
    print('\n-------------------------------------------------')
    print('max palindromes in sequence:')
    logger.info('\n-------------------------------------------------')
    logger.info('max palindromes in sequence:')
    maxPalindromes, maxPalStartIndexes, maxPalLengths = \
        retrievePalindromesFromReducedSet(sequence, palStore_reduced, palindromeStore)
    
    # display maximum palindromes
    for i in range(0, len(maxPalindromes)):
        print('max palindrome: {0}, start index: {1}, length: {2}'.format(
              maxPalindromes[i], maxPalStartIndexes[i], maxPalLengths[i]))
        logger.info('max palindrome: {0}, start index: {1}, length: {2}'.format(
              maxPalindromes[i], maxPalStartIndexes[i], maxPalLengths[i]))
        
    # end timer
    endTime = timer()
    print('\n-------------------------------------------------')
    print('Execution time: {0:6f} seconds'.format(endTime - startTime))
    
    return maxPalindromes