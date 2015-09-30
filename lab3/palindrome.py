#	Jonathan Riordan
#	C13432152
#	Cloud computing

# The scanf, user types in word
word = raw_input("Enter in a word\n")

x = 0


for x in range (len(word) / 2):
	#compare the first letter to the last letter in the word
	if(word[x]) == (word[len(word)-x-1]):
		x += 1
	else:
		t = False
	
	if x == (len(word)/2):
	  t = True
	if x != (len(word)/2):
	  t = False
	
#
if t == True:
	print "True"
else:
	print "False"
	

