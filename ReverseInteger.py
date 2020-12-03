# Question: Reverse an integer
#===========Solution============
# Cleanest solution
def reverse(n):
	r = 0
	# convert int to string and reverse order
	for i in str(n)[::-1]:
		r = r * 10 + int(i)
	return r

# Queue solution
def reverseUsingQueueNoString(n):
	# Convert to array
	arr = []
	while n != 0:
		arr.append(n % 10)
		n = n // 10
	r = 0
	while arr:
		r = r * 10 + arr.pop(0)
	return r

# Tests
assert reverse(1000) == 1
assert reverseUsingQueueNoString(1000) == 1

assert reverse(123) == 321
assert reverseUsingQueueNoString(123) == 321
