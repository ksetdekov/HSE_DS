class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None
        self.depth = 0

    def add(self, value):
        add_node = Node(value)

        if not self.root:
            self.root = add_node
            self.depth = 1
            return

        node = self.root
        curr_depth = 1

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
values = list(map(int, input().split()))[:-1]
for val in values:
    tree.add(val)

print(tree.depth)
