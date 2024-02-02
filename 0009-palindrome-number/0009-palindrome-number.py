class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x%10 == 0 and x!=0):
            return False
        elif list(str(x)) == list(str(x))[::-1]:
            return True
        else:
            return False