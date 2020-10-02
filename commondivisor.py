# Python implementation of program 
from math import sqrt 


# Function to calculate gcd of two numbers 
def gcd(a, b): 
	
	if a == 0: 
		return b 
	return gcd(b % a, a) 
	
# Function to calculate all common divisors 
# of two given numbers 
# a, b --> input integer numbers 
def commDiv(a, b): 
	
	# find GCD of a, b 
	n = gcd(a, b) 

	# Count divisors of n 
	result = 0
	for i in range(1,int(sqrt(n))+1): 

		# if i is a factor of n 
		if n % i == 0: 

			# check if divisors are equal 
			if n/i == i: 
				result += 1
			else: 
				result += 2
				
	return result 

# Driver program to run the case 
if __name__ == "__main__": 
	a = 12
	b = 24; 
	print(commDiv(a, b)) 
