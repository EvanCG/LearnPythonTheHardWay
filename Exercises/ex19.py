def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man thats enough for an awesome party!"
	print "Get a blanket.\n"
	
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can also do math inside:"
cheese_and_crackers(15 - 2, 5 + 10)

print "And we can combine thw two, varables and math:"
cheese_and_crackers(amount_of_cheese -5, amount_of_crackers + 30)