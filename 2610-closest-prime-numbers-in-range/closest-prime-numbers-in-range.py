class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        ans = [True for x in range(right + 2)]
        ans[1] = False
        def primesieve():
            for i in range(2, len(ans)):
                d = 2
                if ans[i] == False:
                    continue
                

                while d*i < len(ans):
                    ans[i*d] = False
                    d += 1
        primesieve()
        primes = []
        for i in range(left, right+1):
            if ans[i] == True:
                primes.append(i)
        result = [-1,-1]
        diff = float('inf')
        for i in range(1,len(primes)):
            if primes[i] - primes[i-1] < diff:
                result = [primes[i-1],primes[i]]
                diff = primes[i] - primes[i-1]
        return result
                