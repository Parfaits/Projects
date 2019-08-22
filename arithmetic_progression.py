"""
Johnny Doan
Algorithm: aProgression(N)
input: takes a positive integer N 
output: returns the number of ways i to express N as a sum of consecutive 
positive integers with n initialized to 2
"""

def aProgression(N):
	i = 0
	n = 2
	while (2*N + n - n**2) > 0:
		a = (2*N + n - n**2)/(2*n)
		if a - int(a) == 0:
			i += 1
			s = 0
			print(f"Initial value found: {a}, with n = {n}\n")
			print("Sequence: ", end='')
			for x in range(int(a), int(a)+n):
				if x == int(a)+n-1:
					print(x, end=' ')
				else:
					print(f"{x} +", end=' ')
				s += x
			if s == N:
				print(f"= N ({N})\n")
			else:
				print(f"!= N ({N}) Error!\n")
		n += 1
	return i

if __name__ == '__main__':
	N = 100
	res = aProgression(N)
	print(f"{res} way(s) to express as a sum of consecutive positive integers.")	