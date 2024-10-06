'''
write a program to read person age from user and check eligible cirteria to see the football match and also print ticket price to the following.

age       ticket price
>=13        15$
>=21        40$
>61&& <=90  25$

'''
age = int(input("Enter your age: "))
if age >= 13 and age <= 90:
    print("You are eligible for seeing the football match.")
    if age >= 13 and age <= 20:
        print("Ticket price is 15$")
    elif age >= 21 and age <= 60:
        print("Ticket price is 40$")
    elif age >= 61 and age <= 90:
        print("Ticket price is 25$")
else:
    print("You are not eligible for seeing the football match.")