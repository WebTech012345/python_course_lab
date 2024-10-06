'''
write to find biggest number among three numbers using if else statement.
'''
a = int(input("enter the value of A : "))
b = int(input("enter the value of B : "))
c = int(input("enter the value of C : "))
if(a>b):
    temp = a
else:
    temp = b
if(temp<c):
    print("Biggest number is ",temp)
else:
    print("Biggest number is ",c)