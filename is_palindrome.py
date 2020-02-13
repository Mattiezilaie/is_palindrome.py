# Author: Mahtab Zilaie
# Date: February 10, 2020
# Description: recursive function that checks if a word is a palindrome


def is_palindrome(word):
    if len(word) <= 1:  # base case - if length of word is less than equal to one
        return True
    if word[0] != word[-1]:   # if first letter of word does not equal last letter
        return False
    return is_palindrome(word[1:-1])  # start from 1 to last index


#print(is_palindrome("racecar"))
#print(is_palindrome("hannah"))
#print(is_palindrome("hello"))
#print(is_palindrome("raciiar"))