class Solution:
    def customSortString(self, order: str, s: str) -> str:
        return [freq:=Counter(s), ''.join([c*freq[c] for c in order] + [c*freq[c] for c in set(s).difference(set(order))])][1]
