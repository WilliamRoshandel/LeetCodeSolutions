class Solution(object):
    def sortString(self, s):
        d = sorted([c, n] for c, n in collections.Counter(s).items())
        result = []
        while len(result) < len(s):
            for i in range(len(d)):
                if d[i][1]:
                    result.append(d[i][0])
                    d[i][1] -= 1
            for i in range(len(d)):
                if d[~i][1]:
                    result.append(d[~i][0])
                    d[~i][1] -= 1
        return ''.join(result)