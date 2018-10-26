113  # Definition for a binary tree node.


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.paths = []

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        def DFS(node, sum, path):
            if node:
                path.append(node.val)
                if sum - node.val == 0 and node.left is None and node.right is None:
                    self.paths.append(path[:])
                    path.pop()
                    return
                elif sum - node.val != 0 and node.left is None and node.right is None:
                    path.pop()
                    return
                DFS(node.left, sum - node.val, path)
                DFS(node.right, sum - node.val, path)
                path.pop()
            # path.pop()

        if not root:
            return self.paths
        DFS(root, sum, [])
        return self.paths


test = '[]'
from treenode import deserialize

root = deserialize(test)
s = Solution()
print(s.pathSum(root, 1))
