# -*- coding: utf-8 -*-

from sys import argv # importing argument support

script, input_file = argv # parsing argument into 2 variables.

def print_all(f): # defining function print_all.
	print f.read() # body of function print_all. Printing whole file.

def rewind(f): # defining function rewind.
	f.seek(0) # body of function rewind. Sets files current position at start.

def print_a_line(line_count, f): # defining function print_a_line. 
	print "current line = %r" % line_count
	print line_count, f.readline() # printing one line and one variable
	
current_file = open(input_file) # openning file

print "First let's print the whole file:\n" # some printing

print_all(current_file) # using function print_all to print file

print "Now let's rewind, kind of like a tape." # sime printing

rewind(current_file) # using function rewind to set file position to beginning

print "Let's print three lines:" # some printing

current_line = 1 # defining variable current_line
print_a_line(current_line, current_file) # function print_a_line that prints out one line and variable

current_line += 1 # variable plus one
print_a_line(current_line, current_file) # function print_a_line that prints out one line and variable

current_line += 1 # variable plus one
print_a_line(current_line, current_file) # function print_a_line that prints out one line and variable
