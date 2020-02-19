p=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
c=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
m='this is an exercise' #input("enter the msg")
s=list(m)

#print(s)

#additive cipher
k1=20 #key value
str1=''
for i in range(len(s)):
	for j in range(len(p)):
		if(s[i]==p[j]):
			t=(j+k1)%26
			str1+=c[t]
print(str1)

#multiplicative cipher
k2=15 #key value
str2=''
for i in range(len(s)):
	for j in range(len(p)):
		if(s[i]==p[j]):
			t=(j*k2)%26
			str2+=c[t]
print(str2)

#Affine cipher
k1=15 #key value
k2=20
str3=''
for i in range(len(s)):
	for j in range(len(p)):
		if(s[i]==p[j]):
			t=(j*k1+k2)%26
			str3+=c[t]
print(str3)
