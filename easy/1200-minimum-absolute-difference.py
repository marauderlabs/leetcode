# https://leetcode.com/problems/minimum-absolute-difference/submissions/

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mindiff = arr[1] - arr[0] #Constraint says, 2 <= arr.length
        result = []

        for i in range(len(arr)-1):
            mindiff = min(mindiff, (arr[i+1] - arr[i]))

        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] == mindiff:
                result.append([arr[i], arr[i+1]])

        return result

