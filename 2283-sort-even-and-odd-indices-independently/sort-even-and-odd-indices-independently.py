class Solution:
    def sortEvenOdd(self, nums):
        even = [0] * 101
        odd = [0] * 101
        n = len(nums)

        for i in range (0, n, 2):
            even[nums[i]] += 1

        for i in range (1, n, 2):
            odd[nums[i]] += 1
        
        k = 0
        for i in range(101):
            while even[i] > 0:
                nums[k] = i
                k += 2
                even[i] -= 1

        k = 1
        for i in range(100, -1, -1):
            while odd[i] > 0:
                nums[k] = i
                k += 2
                odd[i] -= 1

        return nums
        