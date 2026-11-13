class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = []
        for num in nums:
            heapq.heappush(heap, num)    #time = O(nlogk)
        
            if len(heap) > k:
                heapq.heappop(heap)    #time = (klogk)
        
        return heap[0]

        #Overall = O(nlogn) space = O(k)