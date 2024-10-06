''' write a program to initialize student details from the user and print total marks, avarage marks and print also result. '''

'''
variables i need:
1. rollno
2. stname
3. addr
4. phone
5. gender
6. subject1
7. subject2
8. subject3
9. total marks
10. average marks
11. result
'''
rollno = 64
stname = "krishna"
addr = "314, 2nd floor, abc building, xyz street, city"
phone = 9876543210
gender = "male"
subject1 = 56.3
subject2 = 34
subject3 = 78.5
total_marks = subject1 + subject2 + subject3
average_marks = total_marks / 3
#using ternoary operator / conditional operator
result = "pass" if (subject1 >= 35 and subject2 >= 35 and subject3 >= 35) else "fail"
print("rollno: ", rollno)
print("stname: ", stname)
print("addr: ", addr)
print("phone: ", phone)
print("gender: ", gender)
print("subject1: ", subject1)
print("subject2: ", subject2)
print("subject3: ", subject3)
print("total marks: ", total_marks)
print("average marks: ", average_marks)
print("result: ", result)