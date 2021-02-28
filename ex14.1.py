from sys import argv

script, username = argv
prompt = ">"

print "Hello %s !!, Welcome to Jumanji Restro :)" % username
print "May I know what you would like to eat"
print "We have couple of items on our stack"
print """
\t1. Samosa
\t2. Pizza
\t3. Litthi Chokha
\t4. Cold Drinks
"""
print "Please Enter your order from above ^^. Please enter complete order not the numbers"
order = raw_input()
#order = raw_input("Please Enter your order from above ^^. Please enter complete order not the numbers")
print " Please confirm your order %r" % order
print "Thanks for the order, we'll get back to you soon "
