class Solution:
    def fib(self, n: int) -> int:
        queue = deque([0, 1])
        if n <= 1: return queue[n]
        for i in range(2, n+1):
            queue.append(sum(queue))
            queue.popleft()
        return queue[-1]
