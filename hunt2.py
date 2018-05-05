num=input()
d=raw_input()
d=d.split(" ")
d=d[0:num]
for x in sorted(d)[::-1]:
	print x,