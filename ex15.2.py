from sys import argv

print "File name please"
file =  raw_input()

txt = open(file)

print txt.read()
