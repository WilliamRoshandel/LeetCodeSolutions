class Solution(object):
    def majorityElement(self, nums):
        
        majorityElement = len(nums)//2
        hashMap = {}

        for n in nums:
            if n in hashMap:
                hashMap[n] += 1
            else:
                hashMap[n] = 1
        for key, value in hashMap.items():
            if value > majorityElement:
                return key

        return -1



        