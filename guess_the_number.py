import random

def generate_number():
	n = random.randint(1,10)
	return(n)

def check_number(m,n):
	if m == n:
		print("Congratulations!")
	elif m < n:
		m = float(input("Too low, try again:"))
		check_number(m,n)
	else:
		m = float(input("Too high, try again:"))
		check_number(m,n)

n = generate_number()

m = float(input("Guess the number:"))

check_number(m,n)