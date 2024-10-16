class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = ''.join(" " if c in "!?',;." else c for c in paragraph)
        banned = set(banned + [""])
        c = Counter(word for word in map(str.lower, paragraph.split(" ")) if word not in banned)
        return max(c, key=lambda x: c[x])
