class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))
        
        # p, q = {}, {}
        # for a, b in zip(s, t):
        #     if a not in p: p[a]=len(p)
        #     if b not in q: q[b]=len(q)
        #     if p[a] != q[b]: return False
        # return True
