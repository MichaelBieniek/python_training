#https://app.pluralsight.com/player?course=python-getting-started&author=bo-milanovich&name=python-getting-started-m2&clip=0&mode=live

# Python - no typing

answer = 42
pi = 3.14
print(int(answer + pi))

"""comment"""
'comment'
"comment"

# def add_numbers(a, b)
# 	print(a + b)

# add_numbers(5, 5)

# 
print("{0} and {1}".format('apples', 'bananas'))

# String interpolation
print(f"Hi am a {pi} number")

# None as "null"
unassigned_var = None
print(unassigned_var)

# Conditional statements, note the :
number = 5
if number == 5:
	print(f"Number is {number}")
else:
	print(f"Number is not {number}")

# Truthy and falsy
# Truthy a non-zero value, non-blank string, bool true ... like JS

if number and not unassigned_var:
	print("True!")

# Ternary conditionals (like ? :)
a = 1
b = 2
"bigger" if a > b else "smaller"


# ranges
for item in range(5):
	print(item)

# *args similar to rest operator in es6
def func_with_extra_args(id, *args):
	print(args)
# using **kwargs means args stored as dictionary 
func_with_extra_args("1", "2", "3")

# yield and generators
def read_and_yield(f):
	for line in f:
		yield line

# functions
def read_file(file="D:/test.txt"):
	try:	
		f = open(file, "r")
		for line in read_and_yield(f):
			print(line)
		f.close()
	except Exception as e:
		print("Exception {0}".format(e))
read_file()

# lambda functions (a.k.a. () => {})
# anonymous functions
double = lambda x: x * 2
print(double(5))
# useful in higher order functions (HOFs), functions that take functions as params
