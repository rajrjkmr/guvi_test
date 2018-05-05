num=input()
d=raw_input()
d=d.split(" ")
d=d[0:num]
l=[]
for x in range(0,len(d)):
	if x==int(d[x]):
		print x,