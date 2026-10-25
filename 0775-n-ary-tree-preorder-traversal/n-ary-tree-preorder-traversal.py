"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []

        self.dfs(root, result)

        return result

    def dfs(self, root, result):
        if root is None:
            return []
                
        result.append(root.val)

        for child in root.children:
            self.dfs(child, result)
        