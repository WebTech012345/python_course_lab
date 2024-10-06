''' write a program to convert any digit number in terms of years, months and days'''
'''
variables:-
num
years
months
days
'''

num = int(input("Enter any digit numbers: "))
years = num // 365
months = (num % 365) // 30
days = (num % 365) % 30
print("Years: ", years)
print("Months: ", months)
print("Days: ", days)
