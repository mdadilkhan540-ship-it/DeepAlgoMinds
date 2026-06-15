class Solution:
    def countSetBits(self, n):
        if n == 0:
            return 0
        
        # find highest power of 2 <= n
        x = 0
        while (1 << (x + 1)) <= n:
            x += 1
        
        p = 1 << x  # 2^x
        
        # bits till 2^x - 1
        bits_till_p = x * (p >> 1)
        
        # msb contribution from p to n
        msb_bits = n - p + 1
        
        # remaining
        rest = n - p
        
        return bits_till_p + msb_bits + self.countSetBits(rest)
