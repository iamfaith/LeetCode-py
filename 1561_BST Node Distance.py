import tree


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


class Solution:
    """
    @param numbers: the given list
    @param node1: the given node1
    @param node2: the given node2
    @return: the distance between two nodes
    """

    def buildTree(self, nums):
        nodes, root = [None if v == 'null' else TreeNode(int(v)) for v in nums], None
        for node in nodes:
            if root is None:
                root = node
            else:
                prev, cur = None, root
                while cur is not None:
                    prev = cur
                    if node.val < cur.val:
                        cur = cur.left
                    else:
                        cur = cur.right
                if prev.val > node.val:
                    prev.left = node
                else:
                    prev.right = node
            # print node
        return root

    def findLevel(self, root, val):

        def DFS(cur, val, level):
            # not find
            if cur is None:
                return -1

            if cur.val == val:
                return level
            elif cur.val > val:
                level += 1
                return DFS(cur.left, val, level)
            else:
                level += 1
                return DFS(cur.right, val, level)

        return DFS(root, val, 0)

    def findLevelLoop(self, cur, val):
        level = 0
        while cur is not None:
            if cur.val == val:
                return level
            elif cur.val > val:
                level += 1
                cur = cur.left
            else:
                level += 1
                cur = cur.right
        return -1

    def findCommonAncestor(self, nums, n1, n2):
        big, small = max(n1, n2), min(n1, n2)

        for n in nums:
            if small <= n < big:
                return n
        return None

    def bstDistance(self, numbers, node1, node2):
        # Write your code here
        if not numbers.__contains__(node1) or not numbers.__contains__(node2):
            return -1

        ancestor = self.findCommonAncestor(numbers, node1, node2)
        if ancestor is None:
            return -1
        root = self.buildTree(numbers)
        return self.findLevelLoop(root, node1) + self.findLevelLoop(root, node2) - 2 * self.findLevelLoop(root,
                                                                                                          ancestor)

        # tree.drawtree(root)


s = Solution()
print s.bstDistance([2, 16, 7, 5, 20, 18, 6, 8, 13], 11, 18)
