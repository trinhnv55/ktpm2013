#import math

#class tamgiac1 :
	# a=""
	# b=""
	# c=""
	
	# def __init__(self,a,b,c):
		# a = a
		# b = b
		# c = c
import math
	
def detect_triangle(a,b,c):
	epsilon = 1e-14
	if ( a <= 0.0 or a > (2**32 - 1 )  or b <= 0.0 or b > (2**32 - 1)  or c <= 0.0 or c > (2**32 -1 )):
		return "sai gia tri dau vao"
	elif (abs (a) >= abs (b) + abs (c)) or ( abs (b) >= abs (a) + abs (c)) or ( abs (c) >= abs (a) + abs (b)):
		return "khong phai tam giac"
	else:
		if (a == b and b == c ):
			return "tam giac deu"
		else:
			if abs(a*a - b*b - c*c) <= epsilon:
				if b == c :
					return "tam giac vuong can"
				else :
					return "tam giac vuong"
			elif abs(b*b - a*a - c*c) <= epsilon:
				if a == c:
					return "tam giac vuong can"
				else:
					return "tam giac vuong"
			elif abs(c*c - a*a - b*b) <= epsilon:
				if b == a:
					return "tam giac vuong can"
				else :
					return "tam giac vuong"
		
			elif ( a == b or a == c or b == a):
				return "tam giac can"
			else :
				return "tam giac thuong"
