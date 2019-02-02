class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def deserialize(string):
            if string == '{}':
                return None
            nodes = [None if val == 'null' else TreeNode(int(val))
                     for val in string.strip('[]{}').split(',')]
            kids = nodes[::-1]
            root = kids.pop()
            for node in nodes:
                if node:
                    if kids: node.left = kids.pop()
                    if kids: node.right = kids.pop()
            return root

        def dfs(root, p, q):
            if root is not None:
                print root
                if p == root.val:
                    return root
                if q == root.val:
                    return root
                left, right = None, None
                if root.left is not None:
                    left = dfs(root.left, p, q)
                if root.right is not None:
                    right = dfs(root.right, p, q)
                if left is not None and right is not None:
                    return root
                return left if left is not None else right

        return dfs(deserialize(root), p, q)


s = Solution()
print s.lowestCommonAncestor('[3,5,1,6,2,0,8,null,null,7,4]',
                             5,
                             1)
