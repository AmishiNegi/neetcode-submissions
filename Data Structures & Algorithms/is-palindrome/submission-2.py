class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l <= r:
            if (not s[l].isalnum()) and s[r].isalnum():
                l += 1
                continue

            elif s[l].isalnum() and (not s[r].isalnum()):
                r -= 1
                continue
            
            elif s[l].isalnum() and s[r].isalnum() and s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
        return True