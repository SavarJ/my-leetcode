class Solution:
    def oddString(self, words: List[str]) -> str:
        count = idx = 0
        for i in range(1, len(words)):
            if any(a[1]-a[0] != b[1]-b[0] for a, b in zip(pairwise(map(ord, words[0])), pairwise(map(ord, words[i])))):
                count += 1
                idx = i
        
        return words[0] if count == len(words)-1 else words[idx]
