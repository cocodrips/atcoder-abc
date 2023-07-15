import math
import heapq

vectors = [[...]]
new_vector = [...]
distances = []
for i, vector in enumerate(vectors):
    s = 0
    for x1 in vector:
        for x2 in new_vector:
            s += (x1 - x2) ** 2
    d = math.sqrt(s)
    distances.append((d, i))
heapq.heapify(distances)
print(heapq.nsmallest(100, distances))
