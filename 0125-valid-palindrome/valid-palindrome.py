class Solution(object):
    def isPalindrome(self, s):

        palindrome = []

        for char in s:
            if char.isalnum():
                palindrome.append(char.lower())
        return palindrome == palindrome[::-1]




