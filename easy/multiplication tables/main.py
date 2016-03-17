"""
@Project Name - main
@author - Johnathan
@date - 3/16/2016
@time - 7:47 PM

print out 12 by 12 multiple table
"""

for x in xrange(1,13):
    for y in xrange(1,13):
        print "{:>4}".format(str( y * x )),
    print ""