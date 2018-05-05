s=raw_input()
data=s.split(" ")
m=int(data[0])
for x in data:
	x=int(x)
	if m<x:
		m=x
print m