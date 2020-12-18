class Solution:
    def getAllTwoSum(self, A, target):
        # 2 Pointer approach: (assumes solution exists)
        N = len(A)
        if N == 0:
            return []
        i, j = 0, N - 1
        S = A[i] + A[j]
        tuples = []
        while S != target and (i in range(N) and j in range(N)):
            if S < target:
                i += 1
            elif S > target:
                j -= 1
            else:
                break
            S = A[i] + A[j]
        
        while i < j and A[i] + A[j] == target:
            # print('target: ', target)
            # print(A[i], A[j])
            tuples.append([A[i], A[j]])
            i += 1
            j -= 1
            # print(A[i], A[j])

        return tuples

    def getDistinctIndices(self, nums):
        distinctIndices = [0]
        for i in range(len(nums)):
            if nums[i] != nums[distinctIndices[-1]]:
                distinctIndices.append(i)
        return distinctIndices

    def threeSum(self, nums):
        N = len(nums)
        nums.sort()
        print(nums)
        distinctIndices = self.getDistinctIndices(nums)
        triplets = []
        for i in distinctIndices:
            # print(nums[i])
            complement = -nums[i]
            # print('complement', complement)
            d = sorted(list(set(nums[i:])))
            for tupl in self.getAllTwoSum(d, complement):
                triplets.append([nums[i]] + tupl)
        return triplets
    
sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))