# Passed LeetCode, iterative approach beats 96%
class Solution:
    # Array of size n has n! permutations
    # So, best conceivable runtime is O(n!)
    # Let S(n) denote the set of permutations of nums[:n]
    # input: List[int]
    # output: List[List[int]]
    
    # Ex
    # input: [1, 2, 3]
    # [1]
    # [2, 1], [1, 2]
    # [3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]
    # This algorithm has O(n * n!) = O((n + 1)!)
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        if N == 0:
            return 0
        prevPerms = [[nums[0]]]
        currentPerms = []
        for n in range(1, N):
            currentPerms = []
            for perm in prevPerms:
                for insertIndex in range(n + 1): # (length of perm) + 1
                    currentPerms.append(perm[:insertIndex] + [nums[n]] + perm[insertIndex:])
            prevPerms = currentPerms
        return prevPerms
       # Recursive brainstorm.
    # Idea: for every element in nums, call perms with that element removed
    # For every perms returned, iterate through each position 
    # and add the element to the position you removed
    # [1, 2, 3]
    # [2, 3]
    # [2]
    # []
    # [2]
    def permuteRecursive(self, nums: List[int], N=None) -> List[List[int]]:
        if N is None:
            N = len(nums)
        if N == 0:
            return [[]]
        allPerms = []
        removed = nums.pop()
        for perm in self.permute(nums, N - 1):
            for x in range(N):
                allPerms.append(perm[:x] + [removed] + perm[x:])
        return allPerms
        