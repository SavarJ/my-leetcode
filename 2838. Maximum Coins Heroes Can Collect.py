class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        M = sorted(zip(monsters, coins))
        C = [M[0][1]]
        for i in range(1, len(M)):
            C.append(C[-1]+M[i][1])
        
        def bs(hero):
            l, r = 0, len(M)-1
            idx = -1
            while l<=r:
                m = (l+r)//2
                monster = M[m][0]
                if monster > hero:
                    r = m-1
                else:
                    idx = max(idx, m)
                    l = m+1
            
            return 0 if idx == -1 else C[idx]

        return [bs(hero) for hero in heroes]
