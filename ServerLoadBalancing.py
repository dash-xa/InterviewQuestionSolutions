def findClosestValidSum(opt, S, N):
  for s in range(S, -1, -1):
    for n in range(N, -1, -1):
      if opt[n][s]:
        return s 
  return -1

def buildPossibleSumMatrix(A, S, N):
  opt = [[False for s in range(S+1)] for n in range(N+1)]
  opt[0][0] = True
  for n in range(1, N+1):
    for s in range(S+1):
      opt[n][s] = opt[n-1][s]
      if s - A[n-1] >= 0:
        opt[n][s] = opt[n][s] or opt[n-1][s-A[n-1]]
  return opt

# Dynamic programming solution: find subarray which sums as close as possible to sum(A) // 2
# This can be the load of server A. The load of server B is just the complement = sum(A) - load(serverA), 
# so the answer is complement - load(serverA) == sum(A) - 2 * load(serverA)
# This algorithm runs in O(PN) time and O(PN) space, where P is the sum of A and N in the number elements in A
def solution(A):
  P, N = sum(A), len(A)
  opt = buildPossibleSumMatrix(A, P // 2, N)
  return P - 2 * findClosestValidSum(opt, P // 2, N)