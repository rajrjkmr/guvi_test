num=input()
d=raw_input()
d=d.split(" ")
d=d[0:num]
l=[]
for x in d:
	if d.count(x)==1:
		print x,