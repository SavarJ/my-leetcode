class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return len(words) == len(s) and all(word[0] == c for word, c in zip(words, s))
        # return s == ''.join(word[0] for word in words)
