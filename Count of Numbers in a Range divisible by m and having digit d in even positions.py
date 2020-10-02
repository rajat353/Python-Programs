# Python3 Program to find the count of 
# numbers in a range divisible by m 
# having digit d at even positions 

# This Function returns the count of 
# required numbers from 0 to num 
def count(pos, rem, tight, num): 

	# Last position 
	if pos == len(num): 
		if rem == 0: 
			return 1
		return 0
	
	# If this result is already 
	# computed simply return it 
	if dp[pos][rem][tight] != -1: 
		return dp[pos][rem][tight] 

	# If the current position is even, 
	# place digit d, but since we have 
	# considered 0-indexing, check for 
	# odd positions 
	if pos % 2 == 1: 
		if tight == 0 and d > num[pos]: 
			return 0

		currTight = tight 

		# At this position, number 
		# becomes smaller 
		if d < num[pos]: 
			currTight = 1

		res = count(pos + 1, (10 * rem + d) % m, 
								currTight, num) 
		
		dp[pos][rem][tight] = res		 
		return res 
	
	ans = 0

	# Maximum limit upto which we can place 
	# digit. If tight is 1, means number has 
	# already become smaller so we can place 
	# any digit, otherwise num[pos] 
	limit = 9 if tight else num[pos] 

	for dig in range(0, limit + 1): 
		if dig == d: 
			continue

		currTight = tight 

		# At this position, number becomes 
		# smaller 
		if dig < num[pos]: 
			currTight = 1

		# Next recursive call, also set nonz 
		# to 1 if current digit is non zero 
		ans += count(pos + 1, (10 * rem + dig) % m, 
									currTight, num) 
	
	dp[pos][rem][tight] = ans 
	return ans 
	
# Function to convert x into its digit 
# vector and uses count() function to 
# return the required count 
def solve(x): 
	
	global dp 
	num = [] 
	while x > 0: 
		num.append(x % 10) 
		x = x // 10
	
	num.reverse() 
	# Initialize dp with -1 
	dp = [[[-1, -1] for x in range(M)] 
					for y in range(M)] 
	
	return count(0, 0, 0, num) 

# Driver Code 
if __name__ == "__main__": 

	L, R = 10, 99
	
	# d is required digit and number 
	# should be divisible by m 
	d, m = 8, 2
	M = 20
	
	# states - position, rem, tight 
	dp = [] 
	print(solve(R) - solve(L)) 


