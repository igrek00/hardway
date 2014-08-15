# -*- coding: utf-8 -*-

from sys import argv

script, arg1, arg2 = argv

print "script names %r: summator" % script
x = int(arg1) + int(arg2)
print "%r + %r = %r" % (arg1, arg2,x)
