"""
@Project Name - endianness
@author - Johnathan
@date - 11/20/2016
@time - 8:30 PM

"""
import sys
if sys.byteorder == 'little':
    print 'LittleEndian'
else:
    print 'BigEndian'