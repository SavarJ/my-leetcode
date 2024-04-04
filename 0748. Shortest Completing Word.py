class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        return (freq:=Counter(filter(str.isalpha, licensePlate.lower()))) and min((word for word in words if Counter(word)>=freq), key=len)
