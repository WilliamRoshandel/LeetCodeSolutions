class Solution(object):
    def checkIfPangram(self, sentence):
        
        if len(sentence) < 26:
            return False

        for i in range(26):
            if chr(i+97) not in sentence:
                return False
        
        return True

        
        