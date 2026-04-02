class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        absentCount = 0
        lateStreak = 0
        for letter in s:
            if letter == 'A':
                absentCount += 1
                if absentCount >= 2:
                    return False
            if letter == "L":
                lateStreak += 1
                if lateStreak == 3:
                    return False
            else:
                lateStreak = 0    #Resetting the late streak

        return True 
        