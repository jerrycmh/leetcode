class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3 : return 0
        is_prime = [True for _ in range(n)]
        is_prime[0], is_prime[1] = False, False
        counter = 0
        
        for i in range(2, n):
            if is_prime[i]:
                counter += 1
                for p in range(i*2, n, i): is_prime[p] = False
        
        return counter