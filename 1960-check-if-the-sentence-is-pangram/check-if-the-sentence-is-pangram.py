class Solution(object):
    def checkIfPangram(self, sentence):
        
        hashMap = {}

        for i in range(len(sentence)):
            if sentence[i] in hashMap:
                hashMap[sentence[i]] += 1
            else:
                hashMap[sentence[i]] = 1
        for letter in "abcdefghijklmnopqrstuvwxyz":
            if letter not in hashMap:
                return False

        return True

        
        