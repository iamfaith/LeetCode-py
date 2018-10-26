class Solution:
    def convertBST(self, root):
        def DFS(node, val):
            if node.right:
                return DFS(node.right, val)
            node.val += val
            return node.val if node.left is None else DFS(node.left, node.val)

        if root is None:
            return None
        DFS(root, 0)
        return root
