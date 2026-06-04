import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        min_heap = []

        # Step 1: Calculate distance squared and push to the min-heap
        for x, y in points:
            dist_squared = (x ** 2) + (y ** 2)
            # Python sorts by the first element of the tuple (dist_squared)
            heapq.heappush(min_heap, (dist_squared, x, y))
        
        res = []
        # Step 2: Pop out the k elements with smallest distances
        for _ in range(k):
            dist, x, y= heapq.heappop(min_heap)
            res.append([x, y])
        return res
