data=raw_input()
data=data.split(" ")
num=raw_input()
num=num.split(" ")[0:int(data[0])]
sum=0
for x in xrange(0,int(data[1])):
	sum=int(num[x])+sum
print sum