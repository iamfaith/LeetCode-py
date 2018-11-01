from __future__ import print_function
import tree


def printTree(root):
    q = []
    q.append(root)
    last_node, cur_node = root, root
    while len(q) > 0:
        node = q.pop(0)
        print(node, end='')
        if node.left is not None:
            q.append(node.left)
            last_node = node.left
        if node.right is not None:
            q.append(node.right)
            last_node = node.right
        if cur_node == node:
            print('\n')
            cur_node = last_node
            # print("--", cur_node, last_node, q)


root = tree.deserialize('[1,2,3,10,null,4,null,null,5]')
# tree.drawtree(root)
printTree(root)
