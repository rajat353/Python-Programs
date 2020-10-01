while True:
	print("Enter 'x' for exit.")
	num = input("Enter any number: ")
	if num == 'x':
		break
	try:
		number = int(num)
	except ValueError:
		print("Please, enter a number...")
	else:
		rev = 0
		while number > 0:
			rev = (rev*10) + number%10
			number //= 10
		print("Reverse of entered number =",rev)
