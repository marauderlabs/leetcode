# https://leetcode.com/problems/defanging-an-ip-address

class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = ""
        
        for a in address:
            if a == '.':
                result += "[.]"
            else:
                result += a
        
        return result
