# Python3 program for the above approach

# Function to count subarrays in
# which sum of elements at even
# and odd positions are equal
def countSubarrays(arr, n):

	# Initialize variables
	count = 0

	# Iterate over the array
	for i in range(n):
		sum = 0
		
		for j in range(i, n):

			# Check if position is
			# even then add to sum
			# hen add it to sum
			if ((j - i) % 2 == 0):
				sum += arr[j]

			# else subtract it to sum
			else:
				sum -= arr[j]

			# Increment the count
			# if the sum equals 0
			if (sum == 0):
				count += 1
				
	# Print the count of subarrays
	print(count)

# Driver Code
if __name__ == '__main__':

	# Given array arr[]
	arr = [ 2, 4, 6, 4, 2 ]

	# Size of the array
	n = len(arr)

	# Function call
	countSubarrays(arr, n)


