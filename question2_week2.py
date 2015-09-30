#	Jonathan Riordan
#	C13432152
#	Cloud computing
#	Lab-Exercise on Project Euler

num1 = 0
num2 = 1
sum = 0
var = 0

while(sum < 4000000) :
	sum = num1 + num2
	if(sum % 2 == 0) :
		var += sum
		
	num1 = num2
	num2 = sum
	print sum
	

print var


	
	
