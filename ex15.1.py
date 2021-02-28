#from sys import argv

#script, filename = argv

print "Let's not waste any time and tell me the filename you want to open"
filename = raw_input()

txt = open(filename)

print txt.read()
