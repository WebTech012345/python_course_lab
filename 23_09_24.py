'''write a  program to print amount ( HRA(20%), DA(15%)), ALLOWANCES TA (10%) , PF(5%) and gross salary , net salary,
 amount , INCOME TAX (if basic salary  = 15,000 or above (10%,0) '''
'''
variable names :-
1)eid
2)ename
3)addr
4)gender
5)dept
6)desig
7)phone
8)bsal
9)hra
10)da
11)ta
12)pf
13)gross
14)itax
15)net

'''
eid = int(input("enter the value of eid : "))
ename = input("enter the value of ename : ")
addr = input("enter the value of addr : ")
gender = input("enter the value of gender : ")
dept = input("enter the value of dept : ")
desig = input("enter the value of desig : ")
phone = int(input("enter the value of phone : "))
bsal = int(input("enter the value of bsal : "))
hra = bsal * 0.20
da = bsal * 0.15
ta = bsal * 0.10
pf = bsal * 0.05
gross = bsal + hra + da + ta - pf
itax = bsal * 0.10 if bsal >= 15000 else 0
net = gross - itax
print("Allowances amount : ")
print("HRA : ", hra, "\nDA : ", da, "\nTA : ", ta, "\nPF : ", pf,"\nGross salary : ",gross,"\nIncome tax : ",itax,"\nNet salary : ",net)
