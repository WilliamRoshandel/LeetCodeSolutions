class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]
        return ans
