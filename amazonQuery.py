def threeKeywordSuggestions(numreviews, repository, customerQuery):
	# Idea: 
	# 1) Comparisons must be case insensitive, so map everything to lower case
	# 2) Make list of keywords which start with customerQuery. This can be done by looping through repository
	# 3) Sort list to ensure first alphabetical items come first
	# 4) Return first up to 3 items in sorted list
	customerQuery = customerQuery.lower()
	lowerCaseRepo = map(lambda word: word.lower(), repository)
	wordLength = len(customerQuery)
	suggestions = []
	for i in range(2, wordLength):
		validKeywords = []
		for word in lowerCaseRepo:
			if customerQuery[:i] == word[:i]:
				validKeywords.append(word)
		if len(validKeywords) > 0:
			suggestions.append(sorted(validKeywords)[:3])
	return suggestions

repo = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
q = "mouse"
print(threeKeywordSuggestions(5, repo, q))

def getMostFrequentlyUsedWords(literatureText, wordsToExclude):
	# Idea: 
	# 1) count words into hashmap. Ignore words which are wordsToExclude
	# 2) Find most frequent word
	# 3) Return all items such that their count == max count in hashmap
	wordOccurrences = {}
	# map wordsToExclude into hashset for O(1) lookup times
	excludeSet = set(wordsToExclude)
	for word in literatureText.split():
		if word not in excludeSet:
			wordOccurrences[word] = wordOccurrences.get(word, 0) + 1
	if not wordOccurrences:
		return []
	maxCount = max(wordOccurrences.values())
	return list(filter(lambda word: wordOccurrences[word] == maxCount,
						wordOccurrences))

print(getMostFrequentlyUsedWords("al al bal bal", ["al", "bal"]))

def gcd(a, b):  
    if a == 0 : 
        return b  
    return gcd(b % a, a) 

print(gcd(3, 2))