p=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
c=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
m= "XPALASXYFGFUKPXUSOGEUTKCDGFXANMGNVS" #input("enter the msg")
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
	
s=list(m)
#print(s)
#Affine cipher
#key value as ab is encrypted by gl.(0->6, 1->11)
k1=6 #additive key
k2=5 #multicative key
str3=''
for i in range(len(s)):
	for j in range(len(p)):
		if(s[i]==c[j]):
			t=((j-k1)*multi(k2,26))%26
			str3+=c[t]
print(str3)
#plain text=THE BEST OF A FIGHT IS MAKING UP AFTERWARDS

