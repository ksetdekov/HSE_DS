class MaxHeap:
    def __init__(self):
        self.data = []
        self.n = 0

    def sift_down(self, node):
        left_child = node * 2 + 1
        right_child = node * 2 + 2

        if left_child < len(self.data) and self.data[right_child] > max(self.data[node], self.data[left_child]):
            self.data[node], self.data[right_child] = self.data[right_child], self.data[node]
            self.sift_down(right_child)

        elif left_child < len(self.data) and self.data[left_child] > self.data[node]:
            self.data[node], self.data[left_child] = self.data[left_child], self.data[node]
            self.sift_down(left_child)

    def sift_up(self, node):
        if node == 0:
            return

        parent = (node - 1) // 2
        if self.data[parent] < self.data[node]:
            self.data[parent], self.data[node] = self.data[node], self.data[parent]
            self.sift_up(parent)

    def add(self, value):
        self.data.append(value)
        self.n += 1
        self.sift_up(self.n-1)

    def get_max(self):
        self.data[0], self.data[self.n - 1] = self.data[self.n - 1], self.data[0]
        max_val = self.data.pop()
        self.n -= 1
        self.sift_down(0)

        return max_val

heap = MaxHeap()
values = list(map(int, input().split()))[:-1]
for val in values:
    heap.add(val)

print(heap.data)

heap.add(23)
print(heap.data)