#Greatest Common Divisor ,GCD，最大公约数
#欧几里得算法：gcd(a, b) = gcd(b, a mod b)

def gcd_rec(a ,b):
	if b == 0 :
		return a
	else:
		return(gcd, a%b)

def gcd_nonrec(a, b):
	while b > 0:
		r = a % b
		a = b
		b = r
	return a