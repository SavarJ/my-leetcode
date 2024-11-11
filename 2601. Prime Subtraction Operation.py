def primes(n): # simple sieve of multiples from stackoverflow
   odds = range(3, n+1, 2)
   sieve = set(sum([list(range(q*q, n+1, q+q)) for q in odds], []))
   return [2] + [p for p in odds if p not in sieve]

PRIMES = primes(1001)

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        @cache
        def bs(target):
            l, r = 0, len(PRIMES)-1
            
            while l <= r:
                m = (l+r)//2
                if target == PRIMES[m]: return PRIMES[m]
                if target > PRIMES[m]:
                    l = m+1
                else:
                    r = m-1
            
            return 0 if r == -1 else PRIMES[r]

        prev = 0
        for i in range(len(nums)):
            target = nums[i]-prev-1 # try to decrease it as much as possible
            prime = bs(target)
            nums[i] -= prime
            if nums[i] <= prev: 
                return False
            prev = nums[i]
        
        return True
