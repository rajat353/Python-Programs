# Python3 Program to count all subarrays 
# having XOR of elements as given value m 
# with O(n) time complexity. 

# Returns count of subarrays of arr 
# with XOR value equals to m 
def subarrayXor(arr, n, m): 

	ans = 0 # Initialize answer to be returned 

	# Create a prefix xor-sum array such that 
	# xorArr[i] has value equal to XOR 
	# of all elements in arr[0 ..... i] 
	xorArr =[0 for _ in range(n)] 

	# Create map that stores number of prefix array 
	# elements corresponding to a XOR value 
	mp = dict() 

	# Initialize first element 
	# of prefix array 
	xorArr[0] = arr[0] 

	# Computing the prefix array. 
	for i in range(1, n): 
		xorArr[i] = xorArr[i - 1] ^ arr[i] 

	# Calculate the answer 
	for i in range(n): 
		
		# Find XOR of current prefix with m. 
		tmp = m ^ xorArr[i] 

		# If above XOR exists in map, then there 
		# is another previous prefix with same 
		# XOR, i.e., there is a subarray ending 
		# at i with XOR equal to m. 
		if tmp in mp.keys(): 
			ans = ans + (mp[tmp]) 

		# If this subarray has XOR 
		# equal to m itself. 
		if (xorArr[i] == m): 
			ans += 1

		# Add the XOR of this subarray to the map 
		mp[xorArr[i]] = mp.get(xorArr[i], 0) + 1

	# Return total count of subarrays having 
	# XOR of elements as given value m 
	return ans 

# Driver Code 
arr = [4, 2, 2, 6, 4] 
n = len(arr) 
m = 6

print("Number of subarrays having given XOR is", 
						subarrayXor(arr, n, m)) 

# This code is contributed by mohit kumar 
