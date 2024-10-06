''' write a program to swap a two variable values'''

'''
here  i am using only 2 variables not using any extra variable to swap.
variable name :-
1) a
2)b
'''
print("Using python logic:-")

a = int(input("\nenter the value of  'A' : "))
print("\nthe value of 'A' before swapping it  : ",a)
b = int(input("\nenter the value of  'B' : ",))
print("\n the value of 'B' before swapping it : ",b)

a,b = b,a # here is the smiplist  way to swap variable  using  python  (in python it is possiable).

print("\n the value of  'A' after swapping :",a)
print("\n the value of  'B' after swapping :",b)


'''

a = int(input("enter the value of  A : "))
print("the value of A before swapping it  : ",a)
b = int(input("enter the value of  B : "))
print("\n the value of B before swapping it : ",b)

a,b = b,a # here is the smiplist  way to swap variable  using  python  (in python it is possiable).

print("\n the value of  A after swapping :",a)
print("\n the value of  B after swapping :",b)

'''




# if create the same thing using c logic the how it will be :-
print("\n\nUsing C logic:-")

print("\n1)")

a = int(input("\nenter the value of  'A' : "))
print("\nthe value of 'A' before swapping it  : ",a)
b = int(input("\nenter the value of  'B' : ",))
print("\n the value of 'B' before swapping it : ",b)

a=a+b
b= a-b
a= a-b

print("\n the value of  'A' after swapping :",a)
print("\n the value of  'B' after swapping :",b)


print("\n2)")

a = int(input("\nenter the value of  'A' : "))
print("\nthe value of 'A' before swapping it  : ",a)
b = int(input("\nenter the value of  'B' : ",))
print("\n the value of 'B' before swapping it : ",b)

 # here is were are using third variable to create  it.
temp = a
a=b
b= temp



print("\n the value of  'A' after swapping :",a)
print("\n the value of  'B' after swapping :",b)


