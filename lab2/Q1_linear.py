print("enter value of a,c,b and n seperated by  space for linear equation:ax+c=b(mod n)")
a,c,b,n=map(int, input().split())
'''a=int(a)
b=int(b)
c=int(c)
n=int(n)'''
def gcd(a,n):
	r1=r2=r=0
	if(a>n):
		r1=a
		r2=n
	elif(a<n):
		r1=n
		r2=a
	else:
		r1=a
	while(r2>0):
		q=r1//r2
		r=r1-q*r2
		r1=r2
		r2=r
	return r1
def multi(a,n):
	r1=n
	r2=a
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
			#print("inverse of",a,"is ",t1)
		#else:
			#print("inverse of",b,"is ",t1)
		return t1
	else:
		print("inverse does not exist")
	
if(c!=0):
	b=b-c
	if(b<0):
		b=b+n
	d=gcd(a,n)
else:
	d=gcd(a,n)
if(b%d!=0):
	print("NO SOLUTION")
else:
	print(d,"solution")
	a=a//d
	b=b//d
	n1=n//d
	
	x0=(b*multi(a,n1))%n1
	print("solution are ",x0)
	for i in range(1,d):
		x=x0+i*(n/d)
		print(x)
