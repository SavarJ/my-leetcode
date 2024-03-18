class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        return bisect_left(list(accumulate(sorted(capacity)[::-1])), sum(apple))+1
