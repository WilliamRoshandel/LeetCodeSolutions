class Solution(object):
    def minimalKSum(self, nums, k):
        minNum = 1
        total = 0

        for num in sorted(set(nums)):
            missing = num - minNum
            take = min(k, missing)

            # Sum take consecutive integers starting at minNum.
            total += take * (2 * minNum + take - 1) // 2
            k -= take

            if k == 0:
                return total

            minNum = num + 1

        # After the largest existing number, every candidate is missing.
        return total + k * (2 * minNum + k - 1) // 2