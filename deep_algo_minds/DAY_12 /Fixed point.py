class Solution:
    def valEqualToPos(self, arr):
        ans = []

        for i in range(len(arr)):
            if arr[i] == i + 1:
                ans.append(i + 1)

        return ans
    
