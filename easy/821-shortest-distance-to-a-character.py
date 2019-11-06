#https://leetcode.com/problems/shortest-distance-to-a-character


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:

        prev = float('inf')
        result = []
        for i, x in enumerate(S):
            if x == C:
                prev = i
            if prev != float('inf'):
                result.append(i - prev)
            else:
                result.append(float('inf'))


        prev = float('inf')
        for i in range(len(S) - 1, -1, -1):
            if S[i] == C:
                prev = i
            result[i] = min(result[i], prev - i)
        return result
