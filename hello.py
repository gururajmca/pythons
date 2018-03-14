#!/usr/bin/python
print "Well come to ML"
days = ["MON", \
	"TUE", \
	3, \
	"4", \
	"Fri", \
	6.0, \
	7]
print days
if True:
	print "It's True"
	print "One more line in the True block"
else:
	print "It's False"
count = 100;
print count
count = "1000"
print count
count = 12.3
print count
testString = "My Name is Gururaj"
print testString[2:]
print days[2:]

# My Dictionay
phone = 'hello' 
person = { 'name' : 'Gururaj', 'addr': '1233', phone : 1092893783}
print person
print "All Keys"
print person.keys()
print "All Values " 
print person.values()
try:
	fh = open('random.txt', 'a')
	fh.write('new lined added in the file')
except IOError:
	print 'File not Exist'
finally:
	print 'We added into file' 
