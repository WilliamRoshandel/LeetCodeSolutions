class Solution:
    def hasTrailingZeros(self, nums):
        n = len(nums) 
        
        for i in range(n):
            for j in range(n):
                if i != j and (nums[i] | nums[j]) % 2 == 0:
                    return True 
        
        return False 



        