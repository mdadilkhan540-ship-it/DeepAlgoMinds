class Solution:
    def sortedMatrix(self, mat):
        n = len(mat)

        # Flatten matrix
        arr = []
        for row in mat:
            arr.extend(row)

        # Sort all elements
        arr.sort()

        # Fill back into matrix
        k = 0
        for i in range(n):
            for j in range(n):
                mat[i][j] = arr[k]
                k += 1

        return mat
        
        
