# Search in rotated sorted array. 2 Solutions:

# Solution 1, from CtCI:
class Solution:
        def f(self, t, l, h, A):
            m = (l + h) // 2
            if l > h:
                return -1
            L, M, H = A[l], A[m], A[h]
            if M == t:
                return m
            leftIsOrdered = L < M
            rightIsOrdered = M < H
            if leftIsOrdered:
                return self.f(t, l, m - 1, A) if L <= t < M else self.f(t, m + 1, h, A)
            elif rightIsOrdered:
                return self.f(t, m + 1, h, A) if M < t <= H else self.f(t, l, m - 1, A)
            else: # neither half ordered
                left = self.f(t, l, m - 1, A)
                right = self.f(t, m + 1, h, A)
                return right if left == -1 else left
                  
        def search(self, nums: List[int], target: int) -> int:
            # Idea: Either the left half or the right half of the array is sorted
            return self.f(target, 0, len(nums) - 1, nums)
            
# Solution 2, invented myself:
class Solution:
    def search(self, nums, target):
        # Consider pointers, lo and hi, let mid = (lo + hi) // 2
        # Let m = nums[mid], l = nums[lo], h = nums[hi]
        # Since array has been rotated, assume hi < lo
        # 3 cases are possible:
        # 0) l = h + 1: pivot found
        # 1) m >= l (before pivot): move l pointer up, lo = mid
        # 2) m < h (after pivot): move h pointer down, hi = mid
        N = len(nums)
        if N == 1:
            return 0 if target == nums[0] else -1
        lo, hi = 0, N - 1
        if not (nums[lo] < nums[hi]):
            while lo != hi - 1:
                mid = (lo + hi) // 2
                l, m, h = nums[lo], nums[mid], nums[hi]
                if m < h:
                    hi = mid
                else:
                    lo = mid
            lo, hi = hi, lo
        mid = 0
        while lo != hi:
            # print('lo, hi before:', lo, hi)
            if lo > hi:
                mid = (hi - (N - lo)) // 2
                if mid < 0:
                    mid += N
            else:
                mid = (hi + lo) // 2
            print('lo, mid, hi counters:', lo, mid, hi)
            l, m, h = nums[lo], nums[mid], nums[hi]
            print('lo, mid hi values:', l, m, h)
            if m < target:
                lo = mid + 1
                if lo > N - 1:
                    lo -= N
                print(lo)
            elif m > target:
                hi = mid
            else:
                return (N + mid) if mid < 0 else mid
        return lo if nums[lo] == target else -1