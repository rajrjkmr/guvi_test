num=input()
d=raw_input()
d=d.split(" ")
d=d[0:num]
u=[]
for x in d:
	x=int(x)
	if d.count(x)>1:
		if x in u:
			pass
		else:
			u.append(x)
print sorted(u)