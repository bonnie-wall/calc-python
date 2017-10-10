import sys

filename, num1, op, num2 = sys.argv
num1, num2 = int(num1), int(num2)

if op == '+':
	# only supports addition
	print(num1 + num2)
elif op =="-":
	# adds ability to subtract
	print(num1 - num2)
elif op =="*":
	# now includes multiplication
	print(num1 * num2)
elif op =="/":
	#division functionality
	print(num1 / num2)
elif op =="^":
	print(num1 ** num2)
else:
	print "0"
## end of file
## master branch edit
## another master branch edit