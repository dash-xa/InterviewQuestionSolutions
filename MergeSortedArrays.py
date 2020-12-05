# There are 2 variants of this problem. One requires you to modify the array in place, and the other doesn't. Here's the one that does:

# Solution has been tested on LeetCode
# Time complexity: O(n + m). Only linear traversals
# Space Complexity: O(n + m)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        m = len(nums2)
        n = len(nums1) - m
        arr1 = nums1[:n]
        arr2 = nums2
        p1 = 0
        p2 = 0
        while not ((p1 == n) and (p2 == m)):
            current = p1 + p2
            if p1 == n: # copy from arr2
                nums1[current] = arr2[p2]
                p2 += 1
            elif p2 == m: # copy from arr1
                nums1[current] = arr1[p1]
                p1 += 1
            elif arr2[p2] < arr1[p1]:
                nums1[current] = arr2[p2]
                p2 += 1
            else:
                nums1[current] = arr1[p1]
                p1 += 1



# Here's the solution that doesn't require in place modification:
#Q1. There are 2 arrays. Smaller is of size m and has m elements in sorted order. The bigger array is
# of size m+n, where there are only n elements in initial n positions in sorted order. So, last m
# positions are empty in the bigger array. Insert smaller array’s m elements in m + n array has all numbers in sorted order.

# Example : 
# Input Array    N[]={5, 9, 15, 20,,,,,, }  n=4
#                M[]={1, 3, 6, 8, 19, 35}  m=6
# Output array   N[]={1, 3, 5, 6, 8, 9, 15, 19, 20, 35}

#=============Solution===============
# Trivial attempt:
# Time complexity O( (m + n) log(m + n))
# Space complexity O(log (m + n))
def merge_sorted_arrays_trivial(small_arr, big_arr):
	return sorted(small_arr + big_arr[:big_arr.index(None)])

# Better attempt:
# Time complexity: O(m + n)
# Space complexity: O(m + n)
def merge_sorted_arrays(small_arr, dest_arr):
	big_arr = dest_arr[:dest_arr.index(None)]
	S = len(small_arr)
	B = len(big_arr)
	s = 0
	b = 0
	while s + b < S + B:
		n = s + b
		if s < S:
			dest_arr[n] = big_arr[b]
			b += 1
		elif b == B:
			dest_arr[n] = small_arr[s]
			s += 1
		elif small_arr[s] < big_arr[b]:
			dest_arr[n] = small_arr[s]
			s += 1
		else:
			dest_arr[n] = big_arr[b]
			b += 1

#=================Tests====================
N = [5, 9, 15, 20, None, None, None, None, None, None]
M = [1, 3, 6, 8, 19, 35]

O = [1, 3, 5, 6, 8, 9, 15, 19, 20, 35]

assert merge_sorted_arrays_trivial(M, N) == O
merge_sorted_arrays(M, N)
assert N == O
