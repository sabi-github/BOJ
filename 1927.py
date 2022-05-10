# 최소 힙

import heapq
import sys

n = int(sys.stdin.readline().rstrip())
heap = []
for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        try:
            result = heapq.heappop(heap)
            print(result)
        except:
            print(0)
    else:
        heapq.heappush(heap, x)