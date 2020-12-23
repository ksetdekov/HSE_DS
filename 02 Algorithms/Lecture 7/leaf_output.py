# https://informatics.mccme.ru/mod/statements/view.php?id=599&chapterid=761#1

# iterate over a tree increasing

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
        """ todo реализовать add рекурентно"""
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
            elif node.val > add_node.val:
                if not node.left:
                    node.left = add_node
                    self.depth = max(curr_depth, self.depth)
                    return
                else:
                    node = node.left
            else:
                return


tree = BST()
values = list(map(int, input().split()))[:-1]
for val in values:
    tree.add(val)

# print(tree.depth)

def leaf_only(v):
    """выводим только листья"""
    if not v:
        return

    leaf_only(v.left)
    if (v.left is None) & (v.right is None):
        print(v.val)
    leaf_only(v.right)

leaf_only(tree.root)