n=input()
v=['a','e','i','o','u']
c=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
if n  in v:
	print("Vowel")
elif n  in c:
	print("Consonant")
else:
	print("Invalid")
