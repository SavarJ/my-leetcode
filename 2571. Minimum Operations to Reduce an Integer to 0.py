class Solution:
    def minOperations(self, num: int) -> int:
        res = 0
        for i in range(num.bit_length()):
            # if you add 1 and it ends up resulting it less 1s, add it (would happen with consective ones)
            if (num + (1<<i)).bit_count() < num.bit_count():
                num = (num + (1<<i))
                res += 1
        
        return res + num.bit_count() # remove the remaining 1s
