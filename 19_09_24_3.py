#how to reuse existing variables
'''
write a program  to read product details from the user and print total
amount , discount amount (10%, if amount > = 2000),net amount
'''
'''
1)product name
2)product id
3)product quantity 
4)quantity sold 
5)rate
6)discount
7)total amount
8)balance quantity
'''
product = int(input("Enter Product id ="))
print("product  id =",product)
product =  input("Enter Name oƒ product : ")
print("Product Name : ",product)
product = float (input("enter product quantity = "))
print("product quantity = ", product)
qsold = float(input("enter product  quantity sold = "))
print("product quantity sold = ",qsold)
product = product - qsold
print("balance quantity = ",product)
rate = float(input("enter product rate = "))
print("product rate = ",rate)
product = qsold*rate
print("total amount = ",product)
dis = product*0.01 if(product >= 2000 )else 0 
print("discount amount = ",dis)
product = product - dis 
print("Net amount = ",product)
