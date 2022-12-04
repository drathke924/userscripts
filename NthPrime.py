from sys import argv

n = int(argv[1])

primes = [2]
step = 1
current = 3

def square(num):
	return num ** 2

def isPrime(num):
	for x in primes:
		if num % x == 0:
			return 0
	return 1

while len(primes) < n:
	while not isPrime(current):
		current += 1
	primes.append(current)
	step += 1
	current += 1
	if sum(list(map(square, primes))) % step == 0:
		print("Works for " + str(step))
