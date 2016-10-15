"""
@Project Name - main
@author - Johnathan
@date - 3/16/2016
@time - 7:05 PM


"""

import os


data_file = os.path.dirname(os.path.realpath(__file__)) + "\\data"

#file = sys.argv[1]
file = data_file

stats = os.stat(file)
print stats.st_size
