import random

# Miller-Rabin primality test

def miillerTest(d, n):
	
	# Pick a random number in [2..n-2]
	# Corner cases make sure that n > 4
	a = 2 + random.randint(1, n - 4);

	x = pow(a, d, n);

	if (x == 1 or x == n - 1):
		return True;

	# Keep squaring x while one
	# of the following doesn't
	# happen
	# (i) d does not reach n-1
	# (ii) (x^2) % n is not 1
	# (iii) (x^2) % n is not n-1
	while (d != n - 1):
		x = (x * x) % n;
		d *= 2;

		if (x == 1):
			return False;
		if (x == n - 1):
			return True;

	# Return composite
	return False;


def isPrime( n, k, m):
	
	for i in range(k):
		if (miillerTest(m, n) == False):
			return False;

	return True;


def get_primes(n, sample_len=100):
	# Number of iterations of Miller Rabin
	k = 20;
	two = 2**n
	L = []
	interval = 2*random.randint(1,10)
	for m in range(1,10**7 + 1,interval):
		if m%500000 == 0:
			print("Searching primes")
		p = 1+ two*m
		if(isPrime(p,k, m)):
			L.append(p)
			if len(L)==sample_len:
				break
	return L
