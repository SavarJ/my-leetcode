class Solution:
    def invalidTransactions(self, T: List[str]) -> List[str]:
        people = {}
        for transaction in T:
            name,time,amount,city = transaction.split(",")
            if name not in people:
                people[name] = {}
            if city not in people[name]:
                people[name][city] = []
            
            people[name][city].append(int(time))
        
        for person, cities in people.items():
            for items in cities.values():
                items.sort()
        
        def bs(A, target):
            l, r = 0, len(A)-1

            while l <= r:
                m = (l+r)//2

                if target == A[m]: return True
                if target > A[m]:
                    l = m+1
                else:
                    r = m-1
            
            # l should be the val just greater than target or len(A)
            # r should be the val just less than target or -1
            return (l < len(A) and A[l]-target <= 60) or (r >=0 and target-A[r] <= 60)
        
        def isInvalid(name, time, amount, city):
            if int(amount) > 1000: return True
            
            time = int(time)
            # go through all cities for that person and binary search for time
            # if within 60 mins, add to result and continue
            for city_, transactions in people[name].items():
                if city == city_: continue # dont search in the same city
                if bs(transactions, time): return True
            
            return False
        
        res = []
        
        for transaction in T:
            if isInvalid(*transaction.split(",")):
                res.append(transaction)
        
        return res
