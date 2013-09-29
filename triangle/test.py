import unittest
import math
from triangle import detect_triangle


class test(unittest.TestCase):

# sai gia tri dau vao
	
	def test1(self):
		result = detect_triangle(-2.0,5.0,6.0)
		self.assertEqual(result,'sai gia tri dau vao')
	def test2(self):
		result = detect_triangle("3.0",2.5,3.0)
		self.assertEqual(result,'sai gia tri dau vao')
	def test3(self):
		result = detect_triangle("",2.5,3.0)
		self.assertEqual(result,'sai gia tri dau vao')
	def test4(self):
		result = detect_triangle("2**31 -1", "2**31 - 1", 1**-9)
		self.assertEqual(result,'sai gia tri dau vao')
	def test5(self):
		result = detect_triangle(-2.0,-5.0,-6.0)
		self.assertEqual(result,'sai gia tri dau vao')
	def test6(self):
		result = detect_triangle(0,5.0,6.0)
		self.assertEqual(result,'sai gia tri dau vao')
	def test22(self):
		result = detect_triangle(2**32,2**32,2*32)
		self.assertEqual(result,'sai gia tri dau vao')

# khong phai tam giac		

	def test7(self):
		result = detect_triangle(2.0,2.0,4.0)
		self.assertEqual(result,'khong phai tam giac')	
	def test8(self):
		result = detect_triangle(2**31-1,1e-8,3.0)
		self.assertEqual(result,'khong phai tam giac')	
	def test9(self):
		result = detect_triangle(1e-8,1e-8,3.0)
		self.assertEqual(result,'khong phai tam giac')
	
# tam giac deu

	def test10(self):
		result = detect_triangle(2.0,2.0,2.0)
		self.assertEqual(result,'tam giac deu')
	def test11(self):
		result = detect_triangle(1e-10,1e-10,1e-10)
		self.assertEqual(result,'tam giac deu')
	def test12(self):
		result = detect_triangle(2**31 - 1,2**31 - 1,2**31 - 1)
		self.assertEqual(result,'tam giac deu')

# tam giac can
	
	def test13(self):
		result = detect_triangle(2.0,2.0,3.0)
		self.assertEqual(result,'tam giac can')
	def test14(self):
		result = detect_triangle(2**31-1,2**31-1,3.0)
		self.assertEqual(result,'tam giac can')
	def test15(self):
		result = detect_triangle(2**31 -1, 2**31 - 1, 1**-9)
		self.assertEqual(result,'tam giac can')
	
	# gioi han nhan biet tam giac can voi min la 1e-6
	def test23(self):
		result = detect_triangle(2.0,2.0,1e-6)
		self.assertEqual(result,'tam giac can')
	def test24(self):
		result = detect_triangle(2.0,2.0,1e-7)
		self.assertEqual(result,'tam giac vuong') # ket qua tra ve la sai
	
# tam giac vuong
	
	def test16(self):
		result = detect_triangle(3.0,4.0,5.0)
		self.assertEqual(result,'tam giac vuong')
	def test17(self):
		result = detect_triangle(2**15,2**15-1, math.sqrt( (2**15 * 2**15 ) +  ((2**15-1) * (2**15-1)) ) )
		self.assertEqual(result,'tam giac vuong')
	def test18(self):
		result = detect_triangle(1e-10,1e-11,math.sqrt( (1e-10 * 1e-10) + (1e-11 * 1e-11) ) )
		self.assertEqual(result,'tam giac vuong')
	
#tam giac vuong can	
	
	def test19(self):
		result = detect_triangle(3.0,3.0,math.sqrt(18.0))
		self.assertEqual(result,'tam giac vuong can')
	
# tam giac thuong

	def test20(self):
		result = detect_triangle(4.3,5.2,6.1)
		self.assertEqual(result,'tam giac thuong')
	def test21(self):	
		result = detect_triangle(2**32-2,2**32-1,2**32 -3 )
		self.assertEqual(result,'tam giac thuong')
	
if __name__ == '__main__':
	unittest.main()