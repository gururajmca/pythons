#!/usr/bin/python
class EMPClass:
	'This is my emplyoee class'
	empCount = 0
	
	def __init__(self, name, sal):
		self.name = name
		self.sal = sal
		EMPClass.empCount +=1
	
	def displayCount(self):
		print 'Total number of employees %d' % EMPClass.empCount

	def employeeInfo(self):
		print "Name :",self.name," Salary: ", self.sal 

class DEPTClass(EMPClass):
	'This is department class'
	def __init__(self, name, sal, dept):
		EMPClass.__init__(self, name, sal)
		self.dept = dept
	def employeeInfo(self):
		print "Name :",self.name," Salary: ", self.sal , " Dept: ",self.dept 
	 

emp1 = DEPTClass('Sara', 2000, 'Sales')
emp2 = DEPTClass('John', 3000, 'Marketing')
emp1.employeeInfo()
emp2.employeeInfo()
emp1.displayCount()
print 'EMP Class Doc ' , EMPClass.__doc__
print 'DEPT Class Doc ' , DEPTClass.__doc__

	
