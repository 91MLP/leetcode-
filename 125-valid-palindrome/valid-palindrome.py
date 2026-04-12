class Solution(object):
    def isPalindrome(self, s):
        cleaned = []
        for char in s:
            if char.isalnum():
                cleaned.append(char.lower())
        p1=0
        p2=len(cleaned)-1
        while p1<p2:
            if cleaned[p1] != cleaned[p2]:
                return False
            p1+=1
            p2-=1
        return True
        