n=int(input("enter value of n"))
print("additive inverse pairs of set Z",n,"are ")
for i in range(n):
	for j in range(i,n):
		if ((i+j)%n==0):
			t1=(i,j)
			print(t1)
print("multiplicative inverse pairs of set Z",n,"are ")
for i in range(n):
	for j in range(i,n):
		if ((i*j)%n==1):
			t2=(i,j)
			print(t2)
