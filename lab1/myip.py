
import googlesearch

query = "what is my ip"

j=googlesearch.search(query, tld="com", num=10, stop=1, pause=2) 
print(j) 

