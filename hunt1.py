num=input()
d=raw_input()
d=d.split(" ")
d=d[0:num]
u=[]
for x in d:
	if d.count(x)>1:
		if x in u:
			pass
		else:
			u.append(x)
for x in sorted(u):
	print x,