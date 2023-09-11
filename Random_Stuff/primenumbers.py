def isPrime(x):
	if x<2:
		return False
	elif x==2:
		return True
		
	for n in range(2,x):
		if x%n==0:
			return False
	return True

def prime_generator(a,b):
	for number in range (a,b):
		if isPrime(number):
			yield number
		
f=int(input())
t=int(input())

print(list(prime_generator(f,t)))
		

	

