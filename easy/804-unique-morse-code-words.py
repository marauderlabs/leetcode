# https://leetcode.com/problems/unique-morse-code-words/

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        uniq = set()

        for word in words:
            morse = ""
            for c in word:
                morse += codes[ord(c) - ord('a')]

            uniq.add(morse)

        return len(uniq)
