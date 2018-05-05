def prime(num):
	for x in xrange(2,num):
		if num%x==0:
			return 1
		else:
			return 0
num=input()
if prime(num):
	print "no"
else:
	print "yes"
