class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = list(s)
        left = 0

        if len(s) == 1:
            return s

        for right in range(len(chars) + 1):
            if right == len(s) or chars[right] == " ":
                end = right - 1 

                while left < end:
                    chars[left], chars[end] = chars[end], chars[left]
                    left += 1
                    end -= 1

                left = right + 1

        return "".join(chars)