# Takes a couple arguments.
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# Ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# This takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1
	
# This one takes none
def print_none():
	print "Nothing here"
	
print_two("Lewl", "Nice")
print_two_again("Lewl", "Nice")
print_one("Yay!")
print_none()