# -*- coding: utf-8 -*-
cars = 100 # cars we have
space_in_a_car = 4.0 # space in cars for passengers
drivers = 30 # drivers who will work today
passengers = 90 # passenger to deliver today
cars_not_driven = cars - drivers # how many cars are not used today
cars_driven = drivers # how many cars used today
carpool_capicity = cars_driven * space_in_a_car # 
avarage_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers,"drivers avaible."
print "There will be", cars_not_driven, " empty cars today."
print "We can transport", carpool_capicity," people today."
print "We have", passengers, "to carpool today."
print "We need to put about", avarage_passengers_per_car, "in each car."
