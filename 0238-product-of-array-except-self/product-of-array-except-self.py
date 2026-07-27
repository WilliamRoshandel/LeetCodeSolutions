class Solution(object):
    def productExceptSelf(self, nums):
        ans = [1] * len(nums)
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]
        return ans
