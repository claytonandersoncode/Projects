import decimal
from decimal import *

	"""
	Calculates future and present value operations:
	"""

def get_fv(pv,r,t):
	"""
	Calculates future value where:
	PV is present value, 
	r stands for the per annum interest rate,
	t is the time in years(or fraction of a year). 
	"""
	result = (pv * pow((1+r),t))
	
	return result

def get_pv(fv,r,t):
	"""
	Calculates present value where:
	FV is future value, 
	r stands for the per annum interest rate,
	t is the time in years(or fraction of a year). 
	"""
	result = (fv * pow((1+r),-t))
	
	return result	
	
def main():
	operation = input("What do you want to do? (PV,FV):")
	if (operation != 'PV' and operation != 'FV'):
		#invalid operation
		print("You must enter a valid operation")
	else:
		if(operation) == 'PV':
			fv = (float(input("Enter FV:")))
			r  = (float(input("Enter r:")))
			t  = (float(input("Enter t:")))
			print (get_pv(fv,r,t))
			
		else:
			pv = (float(input("Enter PV:")))
			r  = (float(input("Enter r:")))
			t  = (float(input("Enter t:")))
			print (get_fv(pv,r,t))
		
main()
