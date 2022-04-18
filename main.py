import pack.math 
import numpy as np
#import curse

np.zeros((3,4))
#input student
Studentlist = []
print("Please input number of students:")
stunum = int(input())
print("Input info of student(Name and  DoB):")
Studentlistname = pack.math.inputt.number("Student", Studentlist, stunum)

#input course
Courselist = []
print("Please input number of courses:")
cournum = int(input())
print("Input info of course:")
Courselist = pack.math.inputt.number("Course", Courselist, cournum)

#list

print("Student's list")
print("Name")
print(pack.math.list.number("Student",Studentlistname))

print("Course's list")
print(pack.math.list.number("Course",Courselist))

#GPA
marklist = []  





#rounddown 
mark = float(input())
mak = rounddown.roundmark(mark)