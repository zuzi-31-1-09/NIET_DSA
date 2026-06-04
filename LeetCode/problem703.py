import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = nums

        # Turn the nums list into a valid min-heap in-place
        heapq.heapify(self.min_heap)

        # Keep only the k largest elements in the heap
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
    
    def add(self, val: int) -> int:
        # Push the new value into our min-heap
        heapq.heappush(self.min_heap, val)

        # If we exceeded size k, pop the smallest element out
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        # The top of the min-heap is now the kth largest element overall
        return self.min_heap[0]