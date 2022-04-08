import math
import numpy as np
import curse

a = math.inputt()
#input student
Studentlist = []
print("Please input number of students:")
stunum = int(input())
print("Input info of student(Name and  DoB):")
Studentlistname = a.number("Student", Studentlist, stunum)

#input course
Courselist = []
print("Please input number of courses:")
cournum = int(input())
print("Input info of course:")
Courselist = a.number("Course", Courselist, cournum)

#list
b = math.list()
print("Student's list")
print("Name")
print(b.number("Student",Studentlistname))

print("Course's list")
print(b.number("Course",Courselist))

#rounddown 
mark = float(input())
mak = module1.roundmark(mark)


