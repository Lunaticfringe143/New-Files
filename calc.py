from multiprocessing import Value


def add(a, b):
	return a+b
def subtract(a, b):
	return a-b
def multiply(a, b):
	return a*b
def divide(a, b):
	if b == 0:
		raise ValueError("value cannot be divided by zero")
	return a/b