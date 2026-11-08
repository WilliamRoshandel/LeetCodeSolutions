class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        
        extP = 1
        refQ = 1

        while extP != 1000:
            if extP * p == refQ * q:
                if extP % 2 == 0 and refQ % 2 != 0:
                    return 0
                elif extP % 2 != 0 and refQ % 2 == 0:
                    return 2
                elif extP % 2 != 0 and refQ % 2 != 0:
                    return 1
            
            if extP * p > refQ * q:
                refQ += 1
            else:
                extP +=1

        