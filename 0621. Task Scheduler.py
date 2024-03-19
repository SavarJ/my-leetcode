class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cpu = [-val for _,val in Counter(tasks).items()]
        heapify(cpu)
        clock, waiter = 0, []
        while cpu or waiter:
            clock += 1
            if waiter and waiter[0][0] == clock: heappush(cpu, -heappop(waiter)[1])
            if cpu and (val := -heappop(cpu)) > 1: heappush(waiter, (clock+n+1, val-1))
        
        return clock
