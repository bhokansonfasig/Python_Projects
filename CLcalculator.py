from __future__ import division
from math import *
import sys

arguments = sys.argv
arguments.pop(0)

exactmode = False
for i in range(len(arguments)):
    if arguments[i-1]=='-e':
        arguments.remove('-e')
        exactmode = True

arguments[0] = arguments[0].replace('^','**')

print(arguments[0]+' = \n')

ans = eval(arguments[0])
exactans = ans


if exactmode==False:
    print('\t'+str(ans)+'\n')

if exactmode==True:
    print('\t'+str(exactans))
    print('\t'+str(ans)+'\n')
