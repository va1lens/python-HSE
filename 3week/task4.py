"""
https://leetcode.com/problems/count-primes/
?envType=problem-list-v2&envId=array
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        is_prime: list[bool] = [True] * (n + 1)
        i: int = 2
        while i * i <= n:
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
            i += 1
        count: int = 0
        for i in range(2, n):
            if is_prime[i]:
                count += 1
        return count
