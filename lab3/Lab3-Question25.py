#	Jonathan Riordan
#	C13432152
#	Cloud computing
#	Lab-Exercise 25 on Project Euler
#	30/9/2015

num1 = 0
num2 = 1
sum = num2
counter = 0	# this is the index, it counts each time a new number is added to the Fibonacci sequence
bool = True	#
var = ""

# while loop for Fibonacci sequence where the total is less than 4 million
while(len(var) < 1000) : 
	sum = num1 + num2
	var = str(sum)
	
	#Counter increases after a new number is added to the sequence.

	#When the sum is equal to or greater and the boolean variable is true, this if statement will print out the index term obce and then the boolean is set to false.

	num1 = num2
	num2 = sum
	
print var
