# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

print "Hi! I will create file %r" % filename
print "And file it with zeroes."

target = open(filename, "w")
target.write('00000000000000000000000000')
target.close()
print "Done!"

