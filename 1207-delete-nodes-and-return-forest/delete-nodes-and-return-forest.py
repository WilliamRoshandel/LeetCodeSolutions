class Solution:
    def delNodes(self, root, to_delete):
        to_delete = set(to_delete)
        result_set = set([root])

        def dfs(node):
            if not node:
                return None

            result = node
            if node.val in to_delete:
                result = None
                result_set.discard(node)
                if node.left: result_set.add(node.left)
                if node.right: result_set.add(node.right)
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            
            return result  

        dfs(root)
        return list(result_set)