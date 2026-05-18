class Solution:
    def sortEvenOdd(self, nums):
        
        odds = [0] * 101
        evens = [0] * 101
        n = len(nums)

        for i in range (1, n, 2):
            odds[nums[i]] += 1
        for i in range (0, n, 2):
            evens[nums[i]] += 1

        k = 0
        for i in range (101):
            while evens[i] > 0:
                nums[k] = i
                k += 2 
                evens[i] -= 1

        k = 1
        for i in range (100, -1, -1):
            while odds[i] > 0:
                nums[k] = i
                k += 2 
                odds[i] -= 1


        return nums