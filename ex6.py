# -*- coding: utf-8 -*-

x = "There are %d types of people." % 10 # string with one format variable
binary = "binary" # some string
do_not = "don't" # another string
y = "Those who know %s and those who %s." % (binary, do_not) # string with 2 format variables

print x # print one string
print y # print another

print "I said %r" % x # printing string that contains another string
print "I also said: '%s'." % y # same here

hilarious = False # string variable
joke_evaluation = "Isn't that joke so funny!? %r" # string variable that contains another string

print joke_evaluation % hilarious # printing string with another string

w = "That is the left side of..." # define string
e = "a string with a right side." # define string

print w + e # concationation of strings
