p=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
c=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
m="dvvkzecfssprkkve" #input("enter the ciphertext")
s=list(m)
#print(s)

#additive cipher
for k in range(26):
	str1=''
	for i in range(len(s)):
		for j in range(len(p)):
			if(s[i]==p[j] or s[i]==c[j]):
				t=(j-k)%26
				if(t<0):
					t+=26
					str1+=p[t]
				else:
					str1+=p[t]
	print("for k=",k,"plain text is ",str1)

#for k= 17 plain text is  meet in lobby at ten

