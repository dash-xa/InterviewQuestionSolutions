def getFirstOcc(S):
  firstOcc = {}
  for i, char in enumerate(S):
    if char not in firstOcc:
      firstOcc[char] = i
  return firstOcc

def solution(S: str) -> str:
  """
  Idea: 
  1. Build a table mapping a character to its first occurrence in the string
  2. Iterate from the last character in the string. For each character index j, get the index i of its first occurrence in the string
    - s[i:j+1] is then the longest possible consistent fragment of s which ends with j
    - compare the length of this to the max length seen so far. 
    - If it is greater than or equal to the longest consistend fragment seen up to this point, set it as the new return value
  
  The time complexity is O(N), since we scan through the array once to build the index table and again to get the longest consistent string
  The space complexity is O(1), since out index table only has 26 keys (one for each letter)
  """
  firstOcc = getFirstOcc(S)
  bestLength, bestPair = -1, (0, 0)
  for j in range(len(S) - 1, -1, -1):
    i = firstOcc[S[j]]
    length = (j+1) - i
    if length >= bestLength:
      bestLength = length
      bestPair = (i, j)
  return S[bestPair[0]:bestPair[1]+1]
print(solution("dog"))
print(solution("abcde"))
print(solution("foobar"))
print(solution("z"))
