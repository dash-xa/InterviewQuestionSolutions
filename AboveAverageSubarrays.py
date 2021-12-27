"""
A = [1 2 5 0 3]
Try [1], remaining average sum is 10 / 4 = 2.5

Brute force: try every possible subarray. O(N^2) possible subarrays. 
  Comparing sums would take O(N), but we can optimize to be O(1)
  Would run in O(N^2). O(1) space beacuse can do inline computation

Possible optimization: use running sums array

"""

"""
[3 4 2]
i=0, j=0, S=9
  i     j   current   remaining numCurrent  Comment
  0     0   3         6           1         add [0, 0]
  0     1   7         
  currentSum=0 remaining=6
  
"""
def aboveAverageSubarrays(A):
  N, S = len(A), sum(A)
  subarrays = []
  for i in range(N):
    currentSum = 0
    remainingSum = S
    for j in range(i, N):
      currentSum += A[j]
      remainingSum -= A[j]
      
      current = (j+1) - i
      remaining = N - current
      
      currentAverage = currentSum / current
      remainingAverage = 0 if remaining == 0 else remainingSum / remaining
      
      if currentAverage > remainingAverage:
        subarrays.append([i+1, j+1])

  return subarrays
      
A = [3, 4, 2]
print(aboveAverageSubarrays(A))
print(aboveAverageSubarrays([1]))

# Notes: didn't account for division by zero when no remaining items