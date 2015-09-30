#	Jonathan Riordan
#	C13432152
#	Cloud computing
#	Lab-Exercise 25 on Project Euler
#	30/9/2015

num1 = 0
num2 = 1
sum = num2
var = 0
counter = 0	# this is the index, it counts each time a new number is added to the Fibonacci sequence
bool = True	#

# while loop for Fibonacci sequence where the total is less than 4 million
while(sum < 4000000) : 
	sum = num1 + num2
	print sum
	
	#Counter increases after a new number is added to the sequence.
	counter += 1
	
	#When the sum is equal to or greater and the boolean variable is true, this if statement will print out the index term obce and then the boolean is set to false.
	if sum >= 1000 and bool == True:
		print "Index of the first term in the Fibonacci sequence to contain 1000 digits is", counter + 1
		bool = False
		
	
	num1 = num2
	num2 = sum



	
	
