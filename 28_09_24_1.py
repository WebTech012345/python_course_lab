'''
write to find biggest number among three numbers using ladder if statement.
'''
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a > b and a > c:
    print("The biggest number is", a)
elif b > c:
    print("The biggest number is", b)
else:
    print("The biggest number is", c)