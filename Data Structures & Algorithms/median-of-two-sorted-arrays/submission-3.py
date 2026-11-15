class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        a, b = nums1, nums2
        if len(a) > len(b):
            a, b = b, a
        
        total = len(a) + len(b)
        half = total // 2

        l = 0
        r = len(a) - 1

        while True:
            i = (r + l) // 2
            j = half - i - 2
        
            aLeft = a[i] if i >= 0 else float("-inf")
            aRight = a[i + 1] if (i + 1) < len(a) else float("inf")
            bLeft = b[j] if j >= 0 else float("-inf")
            bRight = b[j + 1] if (j + 1) < len(b) else float("inf")

            if aLeft <= bRight and bLeft <= aRight:

                if total % 2 == 1:
                    return min(aRight, bRight)
                else:
                    return ((min(aRight, bRight) + max(aLeft, bLeft)) / 2)

            elif aLeft > bRight:
                r = i - 1
            
            else:
                l = i + 1