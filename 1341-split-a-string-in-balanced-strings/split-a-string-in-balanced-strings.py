class Solution(object):
    def balancedStringSplit(self, s):
        result = 0
        count = 0
 
        for letter in s:
            if letter == "L":
                count += 1
            else:
                count -= 1

            if count == 0:
                result += 1
        return result