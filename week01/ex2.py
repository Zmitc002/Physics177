# Zachary Mitchell
# Physics 177
# Spring 2015
# University of California Riverside
# Assignment 1
# Problem 2

print('\n')

homework = [10, 10, 8, 9.5, 3, 9, 0, 6]
midterm = [10, 10, 10, 10, 8, 5, 10, 7]
project = [9, 10, 10, 6, 10, 6, 8, 9]
grades = []

for x in range(0, 8):
    currentGrade = (homework[x] * 0.4) + (midterm[x] * 0.2) + (project[x] 
    * 0.4)
    
    grades.append(currentGrade)
    
grades = [(round(n, 3)) for n in grades]

for x in range(0, 8):
    print(grades[x])

print('\n')

failedNumber = 0
outstandingNumber = 0

for x in range(0,8):
    if grades[x] < 6:
        failedNumber += 1

    if grades[x] > 9.5:
        outstandingNumber += 1

print"Failed Students: ", failedNumber
print"Failed Grades: "
for x in range(0,8):
    if grades[x] < 6:
        print(grades[x])

print('\n')

print"Outstanding Students: ", outstandingNumber
print"Fraction of Outstanding Students: ", outstandingNumber, "/ 8"

#for x in range(0,8):
#   if grades[x] > 9.5:
#      print(grades[x])

print('\n')

plt.hist(grades,bins= 8)
plt.title("Histrograph of Student Grades")
plt.xlabel("Grades")
plt.ylabel("Frequency")
plt.xlim([4, 10])
plt.show()
plt.savefig('grades_historgraph')

