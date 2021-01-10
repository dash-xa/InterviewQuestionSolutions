class Node:
	def __init__(self, val=None):
		self.val = val
		self.children = [None] * 26

def encode(char):
	return ord(char) - ord('a')
def decode(index):
	return chr(index + ord('a'))

def put(node, word, depth=0):
	if node is None:
		node = Node()
	if depth == len(word):
		node.val = True
		return node
	code = encode(word[depth])
	node.children[code] = put(node.children[code], word, depth + 1)
	return node

def get(node, word, depth=0):
	if node is None:
		return False
	if depth == len(word):
		return node.val or False
	code = encode(word[depth])
	return get(node.children[code], word, depth + 1)


def collect(node, visited="", queue=None):
	if queue is None:
		queue = []

	if node is None:
		return []
	if node.val is True:
		queue.append(visited)
	for i in range(len(node.children)):
		letter = decode(i)
		collect(node.children[i], visited + letter, queue)
	return queue

def prefixes(node, prefix, depth=0):
	if node is None:
		return []
	if depth == len(prefix):
		return collect(node, prefix)
	code = encode(prefix[depth])
	return prefixes(node.children[code], prefix, depth + 1)

def wildcardSearch(node, string, depth=0):
	if string[depth] == ".":
		return collect

def growTrie(wordList):
	root = Node()
	for word in wordList:
		put(root, word)
	return root

def testTrie():
	words = ['ze', "hello", 'hell', 'he', 'hi', 'hot']
	root = growTrie(words)
	words.sort()
	for w in words:
		assert get(root, w)

	words.append('hole')
	words.sort()
	assert not get(root, 'hole')
	put(root, 'hole')
	assert get(root, 'hole')

	p = prefixes(root, 'he')
	assert p == sorted(['he', 'hell', 'hello'])

	p = prefixes(root, '')
	assert p == words

testTrie()

