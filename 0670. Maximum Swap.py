class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(map(int, str(num)))
        m = [(0, 0)]*len(num)

        for i in reversed(range(len(num)-1)):
            if m[i+1][0] >= num[i+1]:
                m[i] = m[i+1]
            else:
                m[i] = [num[i+1], i+1]
        
        for i in range(len(num)):
            big, j = m[i]
            if big > num[i]:
                num[i], num[j] = num[j], num[i]
                break
        
        return int(''.join(map(str, num)))
