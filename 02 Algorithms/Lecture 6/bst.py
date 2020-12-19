class Node:
    def __init__(self, val, left=None, righ=None):
        self.val = val
        self.left = left
        self.right = righ


class BST:
    def __init__(self):
        self.root = None
        self.depth = 0

    def add(self, val):
        add_node = Node(val)

        if not self.root:
            self.root = add_node
            self.depth = 1
            return

        node = self.root
        curr_depth = 0

        while node:
            curr_depth += 1
            if node.val < add_node.val:
                if not node.right:
                    node.right = add_node
                    self.depth = max(curr_depth, self.depth)
                    return
                else:
                    node = node.right
            else:
                if not node.left:
                    node.left = add_node
                    self.depth = max(curr_depth, self.depth)
                    return
                else:
                    node = node.left

    tree = BST()
    vals = list(map(int, input().split()))[:-1]
    for val in vals:
        tree.add(val)

    print(tree.depth)
