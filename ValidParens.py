class Solution:
    def isValid(self, s: str) -> bool:
        counts = []
        for c in s:
            if c in "({[":
                counts.append(c)
            else:
                if not counts:
                    return False
                popped = counts.pop()
                case1 = c == ")" and popped != "("
                case2 = c == "]" and popped != "["
                case3 = c == "}" and popped != "{"
                if case1 or case2 or case3:
                    return False
        return not bool(counts)

d = {}
d[(1,1)] = 7
print(set([1]))