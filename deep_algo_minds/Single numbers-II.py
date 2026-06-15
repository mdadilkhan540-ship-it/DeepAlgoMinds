class Solution:
    def singleNumber(self, nums):
        result = 0
        
        for i in range(32):  # check each bit
            bit_sum = 0
            
            for num in nums:
                if num & (1 << i):
                    bit_sum += 1
            
            if bit_sum % 3:
                result |= (1 << i)
        
        # handle negative numbers (32-bit signed int)
        if result >= 2**31:
            result -= 2**32
        
        return result