class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        result = []
        paths = path.split('/')
        print(paths)
        for path in paths:
            if path == '' or path == '.':
                continue
            elif path == "..":
                if result:
                    result.pop()

            else:
                result.append(path)
            
        return '/' + '/'.join(result)