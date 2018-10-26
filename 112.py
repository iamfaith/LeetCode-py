from treenode import deserialize


class Solution:
    def __init__(self):
        self.find = False

    def hasPathSum(self, root, sum):
        def DFS(node, sum):
            if node:
                if sum - node.val == 0 and node.left is None and node.right is None:
                    self.find = True
                    return
                DFS(node.left, sum - node.val)
                DFS(node.right, sum - node.val)

        if not root:
            return False
        DFS(root, sum)
        return self.find


root = deserialize('[5,4,8,11,null,13,4,7,2,null,null,null,1]')

s = Solution()
print(s.hasPathSum(root, 22))
