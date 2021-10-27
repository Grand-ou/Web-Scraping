import math
gpa = 0.0
total_credits = 0
course1 = input()
credit1 = input()
course2 = input()
credit2 = input()
course3 = input()

credit3 = input()

grade = []
grade.append([course1, credit1])
grade.append([course2, credit2])
grade.append([course3, credit3])
for i in range(3):
    course = grade[i][0]
    credit = grade[i][1]
    #print("cc"+course)
    #print("cc"+credit)
    if (course[0]) == 'A':
        gpa += 4 * float(credit)
    elif (course[0]) == 'B':
        gpa += 3 * float(credit)
    elif (course[0]) == 'C':
        gpa += 2 * float(credit)


    if len(course) == 2 and (course[1] == '+' or course[1] == '-'):
        if course[1] == '+':
            gpa += 0.3 * float(credit)
        if course[1] == '-':
            gpa -= 0.3 * float(credit)
    total_credits += int(credit)
# print (gpa, total_credits)
if total_credits == 0:
    print('0.00')
#elif gpa / total_credits == int(gpa / total_credits):
#    print(str(int(gpa / total_credits)) + '.00')
else:
    aa = gpa / total_credits
    print(aa)
    #print((gpa / total_credits) // 0.01 * 0.01)
    print ((math.floor(aa * 100) / 100.0))


