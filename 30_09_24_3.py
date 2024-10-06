'''
write to find biggest number among three numbers using nested if statement.
'''
a = int(input("enter the value of A : "))
b = int(input("enter the value of B : "))
c = int(input("enter the value of C : "))

if a > b:
    if a > c:
        print("A is the biggest number")
    else:
        print("C is the biggest number")
else:
    if b > c:
        print("B is the biggest number")
    else:
        print("C is the biggest number")