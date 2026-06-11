from typing import List

class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        MOD = 10**9 + 7
        MAX_INV = 400

        req = [-1] * n
        for end, cnt in requirements:
            req[end] = cnt

       
        if req[0] not in (-1, 0):
            return 0

        dp = [0] * (MAX_INV + 1)
        dp[0] = 1

      
        if req[0] == 0:
            pass

        for length in range(2, n + 1):
            ndp = [0] * (MAX_INV + 1)

            window = 0
            for k in range(MAX_INV + 1):
                window = (window + dp[k]) % MOD
                if k >= length:
                    window = (window - dp[k - length]) % MOD
                ndp[k] = window


            required = req[length - 1]
            if required != -1:
                max_possible = length * (length - 1) // 2
                if required > min(MAX_INV, max_possible):
                    return 0

                filtered = [0] * (MAX_INV + 1)
                filtered[required] = ndp[required]
                ndp = filtered

            dp = ndp

        return sum(dp) % MOD
