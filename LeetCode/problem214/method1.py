class Solution:
    def shortestPalindrome(self, s: str) -> str:

        first_half = ""
        for i in range(len(s) - 1, -1, -1):
            import pdb;pdb.set_trace()
            if self.check("%s%s" % (first_half, s)):
                return "%s%s" % (first_half, s)
            first_half += s[i]
        return first_half + s

    @staticmethod
    def check(s):
        if not s and "" == s:
            return False

        end = len(s) - 1
        range_len = len(s) // 2  # 回文 检测一半就行
        for start in range(range_len):
            if s[start] != s[end]:
                return False
            end -= 1
        return True


data="abcbabcab"
result=Solution().shortestPalindrome(data)
print(result)