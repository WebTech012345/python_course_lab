'''write  a program to convert any 3 digit number into reverse order using operators'''

'''
variables names:-
num
'''

num = int(input("enter any 3 digit number: "))
a = num % 10
#print("the value of a is :",a)
b = (num // 10) % 10
#print("the value of b is :",b)
c = (num // 10) // 10
#print("the value of c is :",c)
rev = 0
rev = rev +(a * 100)+(b * 10) + (c * 1)
print("the reverse of the number is :",rev)
