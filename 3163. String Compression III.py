class Solution:
    def compressedString(self, word: str) -> str:
        n = len(word)
        res = []
        l = 0
        for r in range(n+1):
            if r == n or word[r] != word[l] or r-l+1 == 10:
                res.append(str(r-l))
                res.append(word[l])

                l = r
        
        return ''.join(res)
