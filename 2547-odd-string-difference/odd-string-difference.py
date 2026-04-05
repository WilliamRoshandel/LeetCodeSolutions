class Solution(object):
    def oddString(self, words):
        hashmap = defaultdict(list)
        for word in words:
            difference = []
            for i in range(1,len(word)):
                difference.append(ord(word[i])-ord(word[i-1]))
            hashmap[tuple(difference)].append(word)
        for k,a in hashmap.items():
            if len(a) == 1:
                return a[0]
        