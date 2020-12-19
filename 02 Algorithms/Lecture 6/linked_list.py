class LinkedNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, array = []):
        self.head = None
        for i in range(len(array)):

        # for i in range(len(array) - 1, -1, -1):
            self.add(LinkedNode(array[i]))

    def add(self, node):
        node.next = self.head
        self.head = node

    def to_array(self):
        array = []
        node = self.head

        while node:
            array.append(node.val)
            node = node.next
        return array

ll = LinkedList([1, 2,3,4,5])
print(ll.to_array())

