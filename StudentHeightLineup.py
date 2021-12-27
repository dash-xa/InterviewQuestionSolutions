import sys
import bisect

# This solution runs in O(NlogN) time and O(N) space, where N is the number of students
# We use a binary search to find the best row for a student in logN time, and iterate through all students
def solution(A):
  rowMinHeights = [] # sorted array
  for studentHeight in A:
    studentIndex = bisect.bisect_left(rowMinHeights, studentHeight)
    if studentIndex == len(rowMinHeights):
      rowMinHeights.append(studentHeight)
    else:
      rowMinHeights[studentIndex] = studentHeight
  return len(rowMinHeights)


# Solution Brainstorming:
# Can we have students of same height? Could a student stand in that line?
  # Idea: maintain rows array. For each row, we only need to store the minimum height in that row
  # Brute force: For each person, try putting them in every possible row
    # For each person, up to N rows. N people, so grow exponentially
  # optimization: only put students such to decrease rows as little as possible
  
  # [5 4 3 6 1]
  # Student 5 makes own row
  # Student 4 goes to row of student 5
  # Student 3 goes after student 4
  # Student 6 makes new row
  # Student 1 goes after student 3
  
  # Idea: maintain rows list containing shortest student for a given row
  # For each student, get smallest height of student just taller than (or equal to if allowed) given student
  # ceil(rows, student) = index of this student
  # Update row[index] = student height
  # ceil operation is O(N)
  # Iterating through students is also O(N), so overall O(N^2) time complexity
  # Space complexity O(N) due to rows array
  
  # Might be able to optimize floor operation to work in logN time using binary search, so O(NlogN) runtime
  # rows = [3 6 7]
  # ceil(5). Binary search should return index of 6. Then we set 6 -> 5
  # This won't corrupt order of array
  # Suppose we find ceil(3). Then it would return index of 3. So guaranteed to not disturb order
  
  # If we can't find valid row, A[i] is taller than all rows. So we need to make new row
  # Binary search would return N
  # [1 9 3 5 7]
  # rows = [1]
  # [1 9], [1 3], [1 3 5], [1 3 5 7]
  # [1 9], [1 9 3], [1 5 3], 
  # [1 99 2 98 97 96]
  # [1], [1 99], [1 2], [1
  
  # [5 4 3 6 1]
  # rows=[]
  # h = 5. i = 0, so append. rows=[5]
  # h = 4. i = 0, so set rows[0]=4. rows = [4]
  # h = 3. i = 0, so set rows = [4]
  # h = 6. i = 1, so set rows = [4, 6]
  # h = 1. i = 0, so set rows = [1, 6]
  
  # [1]
  # rows=[]
  
  

def main():
  """Read from stdin, solve the problem, write answer to stdout."""
  input = sys.stdin.readline().split()
  A = [int(x) for x in input[0].split(",")]
  sys.stdout.write(str(solution(A)))


if __name__ == "__main__":
  main()
