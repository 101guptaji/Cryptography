n=int(input("enter value of n"))
b=int(input("enter value of b"))
r1=n
r2=b
t1=t=0
t2=1
while(r2>0):
	q=r1//r2
	r=r1-q*r2
	t=t1-t2*q
	r1=r2
	r2=r
	t1=t2
	t2=t
	
	#print(r1,r2)
if(r1==1):
	if(t1<0):
		t1=n+t1
		print("inverse of",b,"is ",t1)
	else:
		print("inverse of",b,"is ",t1)
else:
	print("inverse does not exist")


