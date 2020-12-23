import sys


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def __init__(self, node):
        self.root = node

    def add(self, val):
        add_node = Node(val)

        node = self.root
        prev_node = None
        last = ""

        while node:
            if node.val < add_node.val:
                prev_node = node
                node = node.right
                last = 'r'
            elif node.val > add_node.val:
                prev_node = node
                node = node.left
                last = 'l'
            else:
                return

        if last == "l":
            prev_node.left = add_node
        else:
            prev_node.right = add_node


def traverse(node):
    """traverse для пустого дерева - глубины подревьев считаем"""
    if not node:
        return 0

    depth_l = traverse(node.left)
    depth_r = traverse(node.right)

    if abs(depth_l - depth_r) > 1:
        print("NO")
        sys.exit(0)

    return max(depth_l, depth_r) + 1


vals = list(map(int, input().split()))[:-1]
tree = BST(Node(vals[0]))
for val in vals[1:]:
    tree.add(val)

traverse(tree.root)
print("YES")

