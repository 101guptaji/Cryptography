p=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
c=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
f = [['a',0],['b',0],['c',0],['d',0],['e',0],['f',0],['g',0],['h',0],['i',0],['j',0],['k',0],['l',0],['m',0],['n',0],['o',0],['p',0],['q',0],['r',0],['s',0],['t',0],['u',0],['v',0],['w',0],['x',0],['y',0],['z',0]]
m="ymnxhtzwxjfnrxytuwtanijdtzbnymijyfnqjipstbqjiljtknrutwyfsyyjhmstqtlnjxfsifuuqnhfyntsymfy\
fwjzxjinsymjnsyjwsjyizjytymjgwtfisfyzwjtkymnxknjqiymjhtzwxjhtajwxtsqdxjqjhyjiytunhxkthzxxnslknwxytsxtrj\
fiafshjiytunhxnsnsyjwsjyyjhmstqtlnjxjlbnwjqjxxqfsxrtgnqjnsyjwsjyrzqynhfxyfsiymjsfxjqjhyntstkhzwwjsyfsis\
jcyljsjwfyntsfuuqnhfyntsxfsixjwanhjxjluunuyaatnudtzbnqqqjfwsmtbymjnsyjwsjybtwpxfsimtbxjwanhjxfsifuuqnhf\
yntsxfwjuwtanijiytzxjwxtkymjnsyjwsjyymnxpstbqjiljbnqqmjqudtz"   #input("enter the ciphertext")
s=list(m)
#print(s)
for i in range(len(s)):
	for j in range(len(p)):
			if(s[i]==p[j]):
				f[j][1] = f[j][1] + 1
n = 0
for i in range(26):
    if f[i][1]>n:
        n = f[i][1]
        k = f[i][0]
#print(k,n)
e=p.index('e')
t=p.index(k)
key=t-e
#print(key)

str1=''
for i in m: 
    if i in p:
        j = p.index(i)
        j = (j - key)%26
        str1+=p[j]
    else:
        str1+=i

print("plain text: ",str1)
