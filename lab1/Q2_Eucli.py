#euclidean algo for gcd
x=input("enter two no. for gcd")
a,b=x.split()
a=int(a)
b=int(b)
r1=r2=r=0
if(a>b):
	r1=a
	r2=b
elif(a<b):
	r1=b
	r2=a
else:
	r1=a
#print(r1,r2)
while(r2>0):
	q=r1//r2
	r=r1-q*r2
	r1=r2
	r2=r
	#print(r1,r2)
print("gcd of",a,b,"is ",r1)
