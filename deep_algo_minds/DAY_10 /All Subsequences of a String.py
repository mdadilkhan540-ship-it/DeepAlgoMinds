class Solution:
    def AllPossibleStrings(self, s):
        s = sorted(s)   # ensures lexicographical order
        n = len(s)
        res = []
        
        def dfs(i, path):
            if i == n:
                if path:
                    res.append("".join(path))
                else:
                    res.append("")
                return
            
            # include current character
            dfs(i + 1, path + [s[i]])
            
            # exclude current character
            dfs(i + 1, path)
        
        dfs(0, [])
        
        return sorted(res)
