def func(user_input):
	
	print("Finding check digit for " + user_input + "...")
	padded_user_input = user_input	#padding user input
	if len(user_input) < 11:
		diff = 11 - len(user_input)
		padded_user_input = "0"*diff + user_input

	list_of_nums = [] #queue object here
	for i in range(0,11):
		list_of_nums.append(int(padded_user_input[i]))

	A_val = 0
	B_val = 0
	for i in range(0,11): #setting up calculations
		if (i+1)%2 == 1:
			A_val += list_of_nums[i]
		else:
			B_val += list_of_nums[i]

	M_val = (3 * A_val + B_val)%10 #doing calculations
	if M_val == 0:
		print("check digit: 0")
	else:
		print("check digit: " + str(10-M_val))

	return

if __name__ == "__main__":

	print("gimme the number (11 digits max)") #taking user input
	user_input = input()
	if user_input == "test":
		func("12345")
		func("8675309")
		func("99999999999")
		quit()

	while len(user_input) <= 11 and not user_input.isnumeric(): #checking user input
		print("Oopsie woopsie, you didn't put in a proper integer!")
		user_input = input()

	func(user_input)