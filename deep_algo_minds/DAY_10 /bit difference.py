class Solution:
    def countBitsFlip(self, a, b):
        x = a ^ b   # XOR gives differing bits
        
        count = 0
        while x:
            x = x & (x - 1)  # removes last set bit
            count += 1
        
        return count
    
