# complex numbers in Python
num = 12*0.789
num

big = 1.51547156e23
big

cnum = num + 3.87j
cnum # a complex number where j is an imaginary part
# j is the standard notation to include imaginary parts in a complex number in Python
type(cnum)
# <class 'complex'>

cnum1 = complex(7,6.87)
cnum1 # (7+6.87j)
# so the suffix j indicates that number is the imaginary part of the complex number

# attributes of complex data type
cnum.real 
# 9.468
# .real gives the real part of the complex number

cnum.imag
# 3.87
# .imag gives the imaginary part of the complex number

cnum.conjugate()
# (9.468-3.87j)
# gives the value of imaginary part subtracted from the real part

# complex numbers are useful in defining parameters that has two parts where the second value
# cannot be represented as a decimal
# i.e 10 * second value != first value
# like time: minutes and seconds, degrees(radians)

# complex numbers support mathematical operators but not comparison operators
cnum + cnum1
# (16.468+10.74j)
# addition takes place part wise; real parts are added separately & 
# imaginary parts are added separately

(4.65 + 78.765j) + (87.876 + 68.876j)
# (92.52600000000001+147.64100000000002j)

4.65 + 78.765j + 87.876 + 68.876j
# (92.52600000000001+147.64100000000002j)

complex(12,0.25) / complex(0.25, 0.01)

import cmath
cmath.phase(complex(12,0.345))