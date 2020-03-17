class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        T=haystack
        P=needle

        len_T=len(T)
        len_P=len(P)

        next_list=self.get_next_val(P)
        import pdb;pdb.set_trace()
        if len_P>len_T:
            return -1
        i=0
        j=0
        n=0
        while(i<len_T):
            # print("第{n}轮---------------".format(n=n))
            n+=1
            while(j<=len_P):
                if i>=len_T:
                    break
                # print("###",i,j)
                # print("***",T[i],P[j])
                if T[i]==P[j]:
                    j+=1
                    i+=1
                else:
                    j=next_list[j]
                    i=i                    
                    break
                if (j==len_P):
                    return i-j               
                 
        return -1
    def get_next_val(self,p):

        _next = [0] * (len(p)+1) #      A  B  C  D  A  B  D
        _next[0] = -1            # [-1, 0, 0, 0, 0, 1, 2, 0]
        i, j = 0, -1
        while (i < len(p)):
            # print(i,j)
            # print(p[i] , p[j])
            # import pdb;pdb.set_trace()
            if (j == -1 or p[i] == p[j]):
                i += 1
                j += 1 
                _next[i] = j
            else:
                j = _next[j]
            #print(_next)
        return _next



haystack="hello"
needle="ll"
result=Solution().strStr(haystack,needle)
print(result)