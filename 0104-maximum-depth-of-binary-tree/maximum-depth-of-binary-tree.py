# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        stack = [[root, 1]]
        depth = 0

        while stack:
            node, currDepth = stack.pop()

            if node:
                depth = max(depth, currDepth)
                stack.append([node.left, currDepth + 1])
                stack.append([node.right, currDepth + 1])

        return depth
            
        
        