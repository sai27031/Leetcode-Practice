class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        from typing import List
        from math import gcd
        n = len(coins)
        subsets = []
        for mask in range(1, 1 << n):
            bit = mask & -mask
            i = bit.bit_length() - 1
            prev = mask ^ bit
            if prev == 0:
                L = coins[i]
            else:
                prev_lcm = subsets[prev - 1][0]
                L = prev_lcm // gcd(prev_lcm, coins[i]) * coins[i]
            if L <= min(coins) * k:
                sign = 1 if mask.bit_count() % 2 else -1
                subsets.append((L, sign))
            else:
                subsets.append((L, 0))
        def count(x):
            total = 0
            for L, sign in subsets:
                if L > x:
                    continue
                total += sign * (x // L)
            return total
        left = 1
        right = min(coins) * k
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left