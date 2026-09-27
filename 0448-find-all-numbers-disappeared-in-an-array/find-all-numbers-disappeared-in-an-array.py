class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        n = len(nums)
        
        hashSet =set(range(1, n + 1))
        exists = set(nums)

        for num in hashSet:
            if num not in exists:
                result.append(num)

        return result

        