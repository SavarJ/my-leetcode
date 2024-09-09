class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for word in strs:
            d[tuple(sorted(Counter(word).items()))].append(word)
        return d.values()
