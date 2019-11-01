# https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)

        wrong = 0
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                wrong += 1
        return wrong

