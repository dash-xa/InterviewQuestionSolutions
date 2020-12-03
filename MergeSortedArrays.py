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

N = [5, 9, 15, 20, None, None, None, None, None, None]
M = [1, 3, 6, 8, 19, 35]

O = [1, 3, 5, 6, 8, 9, 15, 19, 20, 35]

assert merge_sorted_arrays_trivial(M, N) == O
merge_sorted_arrays(M, N)
assert N == O
