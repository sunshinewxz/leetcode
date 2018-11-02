class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n,m=len(s),len(p)
        d=[[0]*(m+1) for i in range(n+1)] #d[i,j]=indicator that s[:i] matches with p[:j], for i=0,1,...,n and j=0,1,...,m.
        
        # Boundary conditions
        d[0][0]=1
        for j in range(m):
            if p[j]=='*':
                d[0][j+1]=d[0][j]
        # Recursive update
        for i in range(n):
            for j in range(m):
                if p[j]==s[i] or p[j]=='?':
                    d[i+1][j+1]=d[i][j] 
                elif p[j]=='*': # In this case, p[j] can match with (1) empty sequence, (2) s[i], (3) s[i-k:i+1] for some k.
                                # For case1, we have d[i+1][j+1]=d[i+1][j]; for case2 we have d[i+1][j+1]=d[i][j]; and for
                                # the lase case, we have d[i+1][j+1]=d[i][j+1]. Thus the recursion.
                    d[i+1][j+1]=max(max(d[i][j],d[i+1][j]),d[i][j+1])
                    
        return d[n][m]==1