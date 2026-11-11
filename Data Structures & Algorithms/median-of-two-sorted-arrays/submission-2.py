class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Get total and find half
        a, b = nums1, nums2
        total = len(a) + len(b)
        half = total // 2

        #Identify smaller array
        if len(b) < len(a):
            a,b = b,a
        
        l, r = 0, len(a) - 1
        while True:
            i = (l + r) // 2 #a
            j = half - i - 2 #b, subtract 2 to get rid of index

            aLeft = a[i] if i >= 0 else float("-inf")
            aRight = a[i + 1] if (i + 1) < len(a) else float("inf")
            bLeft = b[j] if j >= 0 else float("-inf")
            bRight = b[j + 1] if (j + 1) < len(b) else float("inf")

            if aLeft <= bRight and bLeft <= aRight:

                if total % 2:
                    return min(aRight, bRight)
                
                return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
            
            elif aLeft > bRight:
                r = i - 1
            else:
                l = i + 1


        
        