# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters

from collections import Counter
from functools import reduce
from typing import Dict

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        def isAllowedWord(allowed: Dict[str, int], freq: Dict[str, int]) -> bool:
            for k, v in freq.items():
                if v > allowed[k]:
                    return False
            return True
            
        
        allowed = Counter(chars)
        result = 0
        
        for w in words:
            freq = Counter(w)
            if isAllowedWord(allowed, freq):
                result += len(w)
        
        return result
