n = raw_input("enter how many fibonacci no u want to print");
a , b = 0 , 1
print a,b
for x in xrange(2,n):
	i = a+b
	print i
	a = b
	b = i
