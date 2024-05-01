class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        return word if (i:=word.find(ch))<0 else word[i::-1]+word[i+1:]
