from input import *
from random import randint
import itertools
import unittest
import re
    
f = open ('input.py')
line = f.readlines()
array = []
numArr = []

for i in range (len(line)):
    if line[i].startswith("def main") and "'''" in line[i+1]:
        for j in range(i+2, len(line)):
            array = re.findall(r'\d+', line[j])
            arr = []
            k = 0
            while k < len(array):
                arr.append(int (array[k]))
                k += 1
            k = 0
            l = 0
            while k < len(arr):
                l = len(arr) - 1
                while l > k :
                    if arr[k] > arr[l-1]:
                        arr[k], arr[l-1] = arr[l-1], arr[k]
                        arr[k+1], arr[l] = arr[l], arr[k+1]
                        l = l-2
                    k += 2
            k = 1
            while k < len(arr):
                l = k+1
                while l < len(arr):
                    if arr[k] >= arr[l]:
                        if(arr[k] > arr[l+1] ):
                            for i in range (k+1, len(arr)-2):
                                arr[i] = arr[i+2]
                            arr[len(arr) - 1] = 'NULL'
                            arr[len(arr) - 2] = 'NULL'
                        else:
                            arr[k] = arr[l+1]
                            for i in range (k+1, len(arr) -  2):
                                arr[i] = arr[i+2]
                            arr[len(arr) - 1] = 'NULL'
                            arr[len(arr) - 2] = 'NULL'
                    else: l += 2
                k += 2
            k = 0
            num = []
            while k < len(arr):
                if arr[k] != 'NULL':
                    num.append(randint(int(arr[k]), int (arr[k+1])))
                k += 2
            numArr.append(num)
            
            if "'''" in line[j]:
                break

for l in range(0,len(numArr)):
    print numArr[l]
class TestSequense(unittest.TestCase):
    pass
def test_generator(a,b):
    def test(self):
        self.assertEqual(a,b)
    return test
if __name__ == '__main__':
    i = 1
    for j in itertools.product(*numArr):
        testName = 'test_%d' % i
        test = test_generator(main(*j),"")
        setattr(TestSequense,testName,test)
        i += 1
    unittest.main()


                    
                
            
