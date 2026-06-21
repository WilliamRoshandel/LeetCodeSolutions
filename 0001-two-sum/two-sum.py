class Solution:
    def twoSum(self, nums, target):
        hashMap = {}

        for i, number in enumerate(nums):
            diff = target - number
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[number] = i
        