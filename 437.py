# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        def DFS(node, sum, path):
            if node:
                return int(sum == node.val) + DFS(node.left, sum - node.val, path) + DFS(node.right, sum - node.val,path)
            return 0

        if not root:
            return 0
        return DFS(root, sum, []) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)


class SolutionBruteForce(object):
    def find_paths(self, root, target):
        if root:
            return int(root.val == target) + self.find_paths(root.left, target - root.val) + self.find_paths(root.right,
                                                                                                             target - root.val)
        return 0

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root:
            return self.find_paths(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return 0


test = '[1,-2,-3,2,3,-2,null,-1]'
# test = '[0,1,1]'
from treenode import *

root = deserialize(test)

s = Solution()
print(s.pathSum(root, -1))
drawtree(root)
