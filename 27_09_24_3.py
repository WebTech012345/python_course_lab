'''
write a program to read any number from the user and check the number is even or odd.
'''
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")