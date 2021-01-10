# made 2 solutions. First uses two-sum like approach, second uses two-sum-sorted like approach with 3 pointers
class Solution:
    
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        
        def getAllTwoSum(A, start, target):
            seen = set()
            valid = []
            for i in range(start, N):
                n = nums[i]
                complement = target - n
                if complement in seen:
                    valid.append(sorted([n, complement]))
                else:
                    seen.add(n)
            return valid

        triplets = set()
        for i in range(N - 2):
            a = nums[i]
            validTuples = getAllTwoSum(nums, i + 1, -a)
            for t in validTuples:
                triplets.add(tuple(sorted([a] + t)))
        return triplets
    
    def threeSum(self, nums):
        N = len(nums)
        nums.sort()
        triplets = set()
        for pa in range(N - 2):
            pb = pa + 1
            pc = N - 1
            while pb < pc:
                S = nums[pa] + nums[pb] + nums[pc]
                if S > 0:
                    pc -= 1
                elif S < 0:
                    pb += 1
                else:
                    triplets.add((nums[pa], nums[pb], nums[pc]))
                    pc -= 1
                    pb += 1
        return triplets
            
            
# Here's 3Sum but with target instead of 0, 3 pointer approach:
class Solution:
    def threeSumTarget(self, nums: List[int], target: int) -> int:
        N = len(nums)
        nums.sort()
        triplets = set()
        for pa in range(N - 2):
            pb, pc = pa + 1, N - 1
            while pb < pc:
                a, b, c = nums[pa], nums[pb], nums[pc]
                S = a + b + c
                # move pointers closer
                if S > target:
                    pc -= 1
                elif S < target:
                    pb += 1
                else:
                    triplets.add((a, b, c))
                    pb += 1
                    pc -= 1
        return triplets
