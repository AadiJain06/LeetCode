from collections import Counter
from typing import List

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        right = Counter(nums)
        left = Counter()

        ans = 0

        for x in nums:
            right[x] -= 1

            target = x * 2

            cnt_left = left[target]
            cnt_right = right[target]

            ans = (ans + (cnt_left * cnt_right) % MOD) % MOD

            left[x] += 1

        return ans % MOD