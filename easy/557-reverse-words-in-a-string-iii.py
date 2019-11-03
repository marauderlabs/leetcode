# https://leetcode.com/problems/reverse-words-in-a-string-iii

# Tried an one-liner. ;-) which is a direct transformation of the function below
class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        for word in s.split():
            result.append(word[::-1])
        return " ".join(result)

# One liner
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([(word[::-1]) for word in s.split()])
       
