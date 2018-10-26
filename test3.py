from tree import *

preNode = TreeNode(-100)


def recoverTree(r):
    inorder_traversal(r)


def inorder_traversal(root):
    if root is not None:
        global preNode
        # print(root.val)
        inorder_traversal(root.left)
        print(str(root.val) + "--" + str(preNode))
        preNode = root
        inorder_traversal(root.right)


root = deserialize('[2,3,4,null,null,1]')
recoverTree(root)
