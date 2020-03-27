class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        right_str=s
        reverse_str=right_str[::-1]
        str_length=len(right_str)

        for i in range(0,str_length):
            a=right_str[0:str_length-i]
            b=reverse_str[i:]

            print(a,b)

            if a==b:
                return reverse_str[:i]+s


s="abcbabcab"

result=Solution().shortestPalindrome(s)
print("")
print("result: ",result)
