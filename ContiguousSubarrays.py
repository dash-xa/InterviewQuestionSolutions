# You are given an array arr of N integers. For each index i, you are required to determine the number of contiguous subarrays that fulfill the following conditions:
# The value at index i must be the maximum element in the contiguous subarrays, and
# These contiguous subarrays must either start from or end on index i.
def count_subarrays(A):
  N = len(A)
  L = [0] # stack
  R = [N-1]
  S = [1] + [0] * (N-1)

  for i in range(1, N):
    while L and A[L[-1]] <= A[i]:
      L.pop()
    if L: S[i] += i - L[-1]
    else: S[i] += i + 1
    L.append(i)
    
    j = (N-1) - i
    while R and A[R[-1]] <= A[j]:
      R.pop()
    if R: S[j] += R[-1] - j
    else: S[j] += i + 1
    S[j] -= 1
    R.append(j)
    
  return S