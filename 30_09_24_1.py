ir=float(input("Enter the initial reading : "))
cr=float(input("Enter the current reading : "))
nou=cr-ir
print("Number of units : ",nou)
if(nou>=1000):
    rpu=9.80
elif(nou>=700):
    rpu=8
elif(nou>=500):
    rpu=6.30
elif(nou>=350):
    rpu=5.50
elif(nou>=200):
    rpu=3.50
elif(nou>=100):
    rpu=1.85
elif(nou<100):
    rpu=0.95
tamt=nou*rpu
sc=tamt*0.07
net=tamt+sc
print("The total amount is : ",tamt)
print("The service charge is : ",sc)
print("The net amount is : ",net)
print("rate per unit : ",rpu)