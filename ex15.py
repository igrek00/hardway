# -*- coding: utf-8 -*-

from sys import argv # importing class argv from module sys

script, filename = argv # saving arguments to script, contains name of script, and filename, first argument

txt = open(filename) # opening file as object txt

print "Here is your file %r:" % filename # printing filename firm first argument
print txt.readline(2) # printing out file
txt.close()
#
#print "Type the filename again:" # printing prompt to enter filename again
#file_again = raw_input("> ") # saving user entered filename
#
#txt_again = open(file_again) # opening new file
#
#print txt_again.readline() # printing new file

#txt_again.close()
