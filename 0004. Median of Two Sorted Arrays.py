class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        if len(B) < len(A):
            A, B = B, A
        
        total = len(A)+len(B)
        half = total//2
        
        # imagine the merged array. there is a left of the median, and right of the median
        # we are binary searching for - how much of the first array is in that left part?
        # once we find it, we can figure out the corresponding other half of the left part and thus the median
        l, r = 0, len(A)-1
        while True:
            i = (l+r)//2
            j = (half - i - 1) - 1

            aleft = A[i] if i>=0 else -inf
            aright = A[i+1] if (i+1) < len(A) else inf
            bleft = B[j] if j>=0 else -inf
            bright = B[j+1] if (j+1) < len(B) else inf

            if aleft <= bright and bleft <= aright:
                if total % 2 == 1:
                    return min(aright, bright)
                else:
                    return (max(aleft, bleft) + min(aright, bright)) / 2
            
            elif aleft > bright:
                r = i-1
            else:
                l = i+1
