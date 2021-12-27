
def getPermutations(arr):
	"""
	Idea: want to compute all permutations of a string 
	Let N be the length of our stirng
		A string has N! permutations
	Best achievable time and space is O(N!)
	
	Are the numbers unique? Yes
	How big can the array length be? up to 6 items

	"abcd"
	_ _ _ _
		a _ _ _
			a b _ _
				a b c _
					a b c d
				a b d _
					a b d c
			a c _ _
			a d _ _
	Backtracking solution: keep track of the path (used indices) and remaining indices (unused). At every point, try using every index
		O(N2^N) time, O(N2^N) space

	[10 20 30 40]
	i=0: try path= [10 0 0 0]
		i=1: try path=[10 20 0 0]
	"""
	perms = []
	def permutations(i, path, remainder):
		if len(remainder) == 0:
			perms.append(path[:])
			return
		rem = remainder[:]
		for element in remainder:
			path.append(element)
			rem.remove(element)
			permutations(i+1, path, rem)
			rem.append(element)
			path.pop()
	permutations(0, [], arr[:])
	return perms
def getPermutationsInString(s):
	return ["".join(l) for l in getPermutations(s)]
print(getPermutations([1, 2, 3]))
# print(getPermutationsInString("abc"))

l = [1, 2, 3]
d = {}
d["a"] = l
l[0] = 10
print(d["a"])