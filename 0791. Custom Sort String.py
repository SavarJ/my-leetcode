class Solution:
    def customSortString(self, order: str, s: str) -> str:
        return [freq:=Counter(s), ''.join([c*freq[c] for c in sorted(ascii_lowercase, key=order.find)])][1]
