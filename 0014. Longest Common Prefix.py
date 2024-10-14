class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        i = 0
        while True:
            curr = set()
            for s in strs:
                if i >= len(s): return ''.join(res)
                curr.add(s[i])
                if len(curr) > 1: return ''.join(res)
                
            res.append(list(curr)[0])
            i += 1
        
        return ''
