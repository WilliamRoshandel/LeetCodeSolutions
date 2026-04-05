class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):

        result = []
        maxVal = max(candies)

        for candy in candies:
            result.append(candy + extraCandies >= maxVal)
        return result
        