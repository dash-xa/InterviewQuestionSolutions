
# Input: List[str] representing lexicographically sorted words
# Output: str representing order of words

# What letters are in the input list? Assume latin alphabet
# Are they all lowercase?
# How big is N?

# Is the answer unique? Not necessarily, return 1 which satisfies it

# "abc", "acb", "bac"
# Ex. words=["dba" "dab" "bad"]
# 1. Know d is before b
# 2. Second character: know b is before a
# Ouput="dba"

# First option: consider all possible orderings of letters, and see if words are sorted according to that order
# 26! possible orderings
# For each ordering iterate through words to determine if that satisfies the ordering
# O(26!N) = O(N). 26! is very big so not practical 

# First character: d before b
# Second character: b before a

# Model problem as a graph. Each letter is a node,
# Each character relation is an edge
# Run topological sort on graph to return valid order of words

# First: consider first char only. Then recurse on all strings with same first char
#  and repeat procedure

# 1. Generate edges for graph
# 2. Run topological sort to obtain valid letter rdering

# ["dba" "dab" "bad"]
# (d, b)
# (b, a)
# valid ordering: "dba"

from collections import defaultdict

# Topological sort with dfs detection
def getLetters(words):
	letters = set()
	for word in words:
		for char in word:
			letters.add(char)
	return letters

# create an edge based on first different char relations 
def getWordEdges(words):
	edges = set()
	for wordA, wordB in zip(words, words[1:]):
		for charA, charB in zip(wordA, wordB):
			if charA != charB:
				edges.add((charA, charB))
				break
	return edges

def getAdjacencyList(edges):
	adj = defaultdict(set)
	for fr, to in set(edges):
		adj[fr].add(to)
	return adj

def buildTopologicalPath(letter, adj, path, seen, order):
	if letter in path:
		path.clear() # we've found a cycle
	elif letter not in seen:
		seen.add(letter)
		path.append(letter)
		for to in adj[letter]:
			buildTopologicalPath(to, adj, path, seen, order)
		if path:
			order.append(path.pop(-1))
		

def getTopologicalOrder(letters, adj):
	order = []
	seen = set()
	for letter in letters:
		if letter not in seen:
			buildTopologicalPath(letter, adj, [], seen, order)
	return order[::-1]

def getWordOrder(words):
	letters = getLetters(words)
	edges = getWordEdges(words)
	adj = getAdjacencyList(edges)	
	order = getTopologicalOrder(letters, adj)
	return "" if len(order) != len(adj) else ''.join(order)	

def testWordOrderImplementation(getWordOrder):
	words = ["dba", "dab", "bad"]
	assert getWordOrder(words) == "dba"

	words = [
	  "wrt",
	  "wrf",
	  "er",
	  "ett",
	  "rftt"
	]
	assert getWordOrder(words) == "wertf"


	words = [
	  "z",
	  "x"
	]
	assert getWordOrder(words) == "zx"

	words = [
	  "z",
	  "x",
	  "z"
	]
	assert getWordOrder(words) == ""

testWordOrderImplementation(getWordOrder)

# Get indegrees of each nodes
def getInDegrees(edges):
	inDegrees = defaultdict(int)
	for fr, to in edges:
		inDegrees[to] += 1
	return inDegrees

# Topological sort using bfs implementation
def getTopologicalOrderUsingBFS(letters, edges, adj):
	inDegrees = getInDegrees(edges)
	order = []
	process = [letter for letter in letters if inDegrees[letter] == 0]
	while process:
		node = process.pop()
		order.append(node)
		for child in adj[node]:
			inDegrees[child] -= 1
			if inDegrees[child] == 0:
				process.append(child)
	return "" if len(order) != len(letters) else ''.join(order)


def getWordOrderUsingBFS(words):
	letters = getLetters(words)
	edges = getWordEdges(words)
	adj = getAdjacencyList(edges)
	order = getTopologicalOrderUsingBFS(letters, edges, adj)
	return order

testWordOrderImplementation(getWordOrderUsingBFS)