class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = 'aeiouAEIOU'
        reversedVowels = []
        for char in s:
            if char in vowels:
                reversedVowels.append(char)
        
        reversedVowels = reversedVowels[::-1]

        s = list(s)
        j = 0
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = reversedVowels[j]
                j += 1
        
        return "".join(s)
        