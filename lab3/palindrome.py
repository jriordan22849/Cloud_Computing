#	Jonathan Riordan
#	C13432152
#	Cloud computing
word = raw_input("enter in a string\n")
x = 0
for i in range (len(word) / 2):
	if(word[x]) == (word[len(word)-x-1]):
		x += 1
	if x == (len(word)/2):
	  t = True
	if x != (len(word)/2):
	  t = False
	
if t == True:
	print "True"
else:
	print "False"
	

