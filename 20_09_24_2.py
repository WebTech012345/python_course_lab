'''write  a program to sum of 3 digit  number using operators'''

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
sum = a + b + c
print("the sum of the digits of the number is :",sum)