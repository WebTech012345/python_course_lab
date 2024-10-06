''' write a program to read  and store student, details from the user at run time  and print total marks, average 
marks and print also result '''


'''
variables names :- 
1)rollno
2)stname
3)addr
4)gender
5)phone
6)sub1
7)sub2
8)sub3
9)total
10)avg
11)result

'''

rollno = input("enter your Roll number : ")
stname = input("enter your full name : ")
addr = input("enter your address : ")
gender = input("enter your gender : ")
phone = input("enter your phone number : ")
sub1 = float(input("enter your subject 1 marks : "))
sub2  = float(input("enter your subject 2 marks : "))
sub3 = float(input("enter your subject 3 marks : "))
total = sub1+sub2+sub3
avg = total / 3
result = "pass" if(sub1 >= 35 and sub2>= 35 and sub3 >= 35) else "fail"

print(rollno,"\n",stname,"\n",addr,"\n",gender,"\n",phone,"\n",sub1,"\n",sub2,"\n",sub3,"\n",total,"\n",avg,"\n",result)
