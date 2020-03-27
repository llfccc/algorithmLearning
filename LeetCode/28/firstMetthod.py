class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        len_T=len(haystack)
        len_P=len(needle)

        if len_P>len_T:
            return -1

        while(i<len_T and j<len_P):
            if 

        for i in range(len_T-len_P+1):
            for j in range(len_P):
                if haystack[i+j]!=needle[j]:
                    break
                if j==len_P-1:
                    return i
        return -1

haystack="aaa"
needle="aaa"
result=Solution().strStr(haystack,needle)
print(result)