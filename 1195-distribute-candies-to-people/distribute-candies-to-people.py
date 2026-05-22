class Solution(object):
    def distributeCandies(self, candies, num_people):
       
        candyDistributionArray = [0] * num_people
        n = 0

        while candies > 0:
            candyDistributionArray[n % num_people] += min(candies, n + 1)
            n += 1
            candies -= n
                
        return candyDistributionArray