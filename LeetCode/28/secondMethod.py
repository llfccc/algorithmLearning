class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        T=haystack
        P=needle

        len_T=len(T)
        len_P=len(P)

        next_list=self.get_next_val(P)
        print(next_list)
        return 
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
        next_list=[-10]*len(p)
        next_list[0] = -1
        j = 0
        k = -1
        while j < len(p) - 1:
            print("*****",j,k)
            print("#####",p[j],p[k])
            if k == -1 or p[j] == p[k]:
                j = j + 1
                k = k + 1
                next_list[j] = k
            else:
                k = next_list[k]
        return next_list





haystack="hello24234234df"
needle="ababababe"
result=Solution().strStr(haystack,needle)
print(result)