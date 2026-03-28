class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):

        maxCandies = max(candies)
        result = []

        for candy in candies:
            if candy + extraCandies >= maxCandies:
                result.append(True)
            else:
                result.append(False)
        
        return result
        