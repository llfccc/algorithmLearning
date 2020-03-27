class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        import pdb;pdb.set_trace()

        if not needle:
            return 0
        T=haystack
        P=needle

        len_T=len(T)
        len_P=len(P)

        next_list=self.get_next_val(P)
        if len_P>len_T:
            return -1
        i=0
        j=0

        while(i<len_T and j<len_P) :
                if T[i]==P[j]:  # 如果符合，则对比下一个字符
                    j+=1
                    i+=1
                elif j==-1: # 如果跳转到了P的首个字符，则让对比下一个字符
                    j+=1
                    i+=1
                else:
                    j=next_list[j]  # 如果对比不符合，则跳转到next数组对应的p去
                    i=i  

                if (j==len_P):
                    return i-j               
                 
        return -1

    def get_next_val(self,p):
        next_list=[-10]*(len(p)+1)
        next_list[0] = -1
        j = 0
        k = -1
        while j < len(p)-1 :
            if k == -1 or p[j] == p[k]:
                j  += 1
                k  += 1
                next_list[j] = k
            else:
                k = next_list[k]      #整个函数最关键的一句，用来依靠前缀和后缀相同的特性来跳过一些情况减少复杂度
        return next_list





haystack="mississippi"

needle="a"
result=Solution().strStr(haystack,needle)
print(result)