# InterviewQuestionSolutions
My solutions to various interview algorithm questions. These are from LeetCode, Cracking the Coding Interview, or other interesting problems.

Each file contains a problem description, as well as my solution followed by a test case.

## General Tips
- Before writing any code, you MUST work through a couple exmamples. Even if you have the algorithm ready. See how your brain would solve it anyways. You should be doing this during the interview
- "Edge check" - After writing your code, take the time to work your code through 1) a normal example, 2) a more tricky normal example, 3) an edge case (null values or something like that)
- When your solution is in a class, don't forget to "self check" after finishing -- a self check is going over the code and making sure that all class variables and methods have a "self." in front of them
- If you get stuck, draw pictures of examples! Can't stress how important this is
- Deal with edge cases (check for null values) at the start of the method
- Tip: When making recursive calls, always make sure you make them with the right parameters!! Avoid stack overflow infinite recursion

### Binary Trees
- Goto algorithms: Inorder traversal, bfs, dfs
- First questions should be:
    - Is the tree a BST?
    - Can nodes have null values? Can these nodes have children?
- If you want to check whether a node has a null value, don't use implicit boolean comparison.
  - (if not node.val) evaluates to true both in cases where node.val = None and where node.val = 0. Watch out for this
