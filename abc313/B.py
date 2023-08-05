from collections import defaultdict
import heapq
import queue


class Node:
    def __init__(self, num):
        self.num = num
        self.weak = []
        self.strong = []

    def __repr__(self):
        return f"Node({self.num}, weak: {self.weak}, strong: {self.strong})"


N, M = list(map(int, input().split(' ')))
strongest = []
A = []
B = []
for i in range(M):
    a, b = list(map(int, input().split(' ')))
    A.append(a)
    B.append(b)

nodes = {}
weaks = set()
for weak, strong in zip(B, A):
    if weak not in nodes:
        nodes[weak] = Node(weak)
    if strong not in nodes:
        nodes[strong] = Node(strong)
    nodes[weak].strong.append(strong)
    weaks.add(weak)

# print(weaks)
# print("nodes", nodes)

strongest = set()
for i in range(1, N + 1):
    if i in weaks:
        continue
    if i not in nodes:
        print(-1)
        exit()
    queue = [nodes[i]]
    while True:
        node = queue.pop(0)
        if not node.strong:
            strongest.add(node.num)
            break
        for strong in node.strong:
            queue.append(nodes[strong])

if len(strongest) == 1:
    print(list(strongest)[0])
else:
    print(-1)
