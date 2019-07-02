#Returns the sum of num1 & num2
def add(num1,num2):
	return num1 + num2
#Returns the result of num1 subtracted by num2
def sub(num1,num2):
	return num1 - num2
#Returns the product of num1 multiplyed by num2
def mul(num1,num2):
	return num1 * num2
#Returns the remainder of num1 divided by num2 
def div(num1,num2):
	return num1 / num2
	
def main():
	operation = input("What do you want to do (+,-,*,/):")
	if (operation != '+' and operation != '-' and operation != '*' and operation != '/'):
		#invalid operation
		print("You must enter a valid operation")
	else:
		num1 = int(input("Enter num1:"))
		num2 = int(input("Enter num2:"))
		if(operation) == '+':
			print (add(num1,num2))
		elif(operation) == '-':
			print (sub(num1,num2))
		elif(operation) == '*':
			print (mul(num1,num2))
		else:
			print (div(num1,num2))

main()

