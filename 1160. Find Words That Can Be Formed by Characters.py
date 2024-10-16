class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        return sum(len(word) for word in words if Counter(word) <= Counter(chars))
