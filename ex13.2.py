# -*- coding: utf-8 -*-

from sys import argv

script_name, arg1, arg2, arg3, arg4 = argv

print "Hi, my name is %r.", script_name
print "You entered four arguments: %r, %r, %r and %r" % (arg1, arg2, arg3, arg4)
print "Yes, it's so simple!"
print "%r\n%r\n%r\n%r\n" % (arg1, arg2, arg3, arg4)
print "Let's calculate a bit!"
add1 = int(raw_input("First addendum is:"))
add2 = int(raw_input("Second addendum is:"))
print "Result is %r" % (add1 + add2)
