class Solution:
    def stringSequence(self, target: str) -> List[str]:
        res = []
        curr = []
        for i in range(len(target)):
            curr.append("a")
            res.append(''.join(curr.copy()))
            while curr[-1] != target[i]:
                curr[-1] = chr(ord(curr[-1])+1)
                res.append(''.join(curr.copy()))
            
        return res
