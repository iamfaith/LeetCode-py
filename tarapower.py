class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


def sortedArrayToBST(arr):
    if not arr:
        return None

    mid = (len(arr)) // 2
    root = TreeNode(arr[mid])
    root.left = sortedArrayToBST(arr[:mid])
    root.right = sortedArrayToBST(arr[mid + 1:])
    return root


def drawtree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1

    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y - 20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x - dx, y - 60, dx / 2)
            jumpto(x, y - 20)
            draw(node.right, x + dx, y - 60, dx / 2)

    import turtle
    t = turtle.Turtle()
    t.speed(0);
    turtle.delay(0)
    h = height(root)
    jumpto(0, 30 * h)
    draw(root, 0, 30 * h, 40 * h)
    t.hideturtle()
    turtle.mainloop()


class Solution:
    def subStringKDist(self, inputStr, num):
        ret, n = set(), len(inputStr)

        for i in range(n):
            dist = 0
            cnt = [0 for x in range(26)]
            temp = []
            for j in range(i, n):
                pos = ord(inputStr[j]) - ord("a")
                if cnt[pos] == 0:
                    dist += 1
                temp.append(inputStr[j])
                cnt[pos] += 1
                if dist == num:
                    # print(temp)
                    tempStr = ''.join(temp)
                    if len(tempStr) == num:
                        ret.add(tempStr)

        return list(ret)

    def bstDistance(self, value, n, node1, node2):
        root = build_tree(value)
        if root.left:
            self.bstDistance(root.left)
        res = min(res, root.val - pre)
        pre = root.val
        if root.right:
            self.bstDistance(root.right)
        return res


def build_tree(lists):
    nodes = [None if val == 'null' else TreeNode(int(val)) for val in lists]
    root, count = nodes[0], len(nodes)
    for i in range(1, count):
        temp = root
        previous = None
        while temp is not None:
            previous = temp
            if temp.val > nodes[i].val:
                temp = temp.left
            else:
                temp = temp.right

        if previous.val > nodes[i].val:
            previous.left = nodes[i]
        else:
            previous.right = nodes[i]

    return root


def pathToNode(root, path, k):
    # base case handling
    if root is None:
        return False

        # append the node value in path
    path.append(root.val)

    # See if the k is same as root's data
    if root.val == k:
        return True

    # Check if k is found in left or right
    # sub-tree
    if ((root.left != None and pathToNode(root.left, path, k)) or
            (root.right != None and pathToNode(root.right, path, k))):
        return True

    # If not present in subtree rooted with root,
    # remove root from path and return False
    path.pop()
    return False


def distance(root, data1, data2):
    if root:
        # store path corresponding to node: data1
        path1 = []
        pathToNode(root, path1, data1)
        print(path1)
        # store path corresponding to node: data2
        path2 = []
        pathToNode(root, path2, data2)
        print(path2)
        # iterate through the paths to find the
        # common path length
        i = 0
        while i < len(path1) and i < len(path2):
            # get out as soon as the path differs
            # or any path's length get exhausted
            if path1[i] != path2[i]:
                break
            i = i + 1
        print(i)
        # get the path length by deducting the
        # intersecting path length (or till LCA)
        return (len(path1) + len(path2) - 2 * i)
    else:
        return 0


s = Solution()
print(s.subStringKDist("abcd", 3))
print(s.subStringKDist("awaglknagawunagwkwagl", 4))
root = build_tree([5, 6, 3, 1, 2, 4])
print(distance(root, 4, 2))
