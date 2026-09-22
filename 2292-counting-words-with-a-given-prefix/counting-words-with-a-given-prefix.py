class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        plen = len(pref)
        count = 0
        for word in words:
            if len(word) < plen:
                continue
            Match = True
            for i in range(plen):
                if word[i] != pref[i]:
                    Match = False
                    break

            if Match:
                count += 1

        return count
        