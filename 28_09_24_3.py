'''
write  a program to read intial reading value,final reading value and print number-of-units ,
 rate-per-units,total amount, service charge (7% on the total amount),net amount(total amount + service amount)


>=1000 9.80
>=700  8.00
>=500  6.30
>=350  5.50
>=200  3.50
>=100  1.85
<100  0.95

variable names :-
i)input:-
invalue -to read intial reading value entered in meter
finalvalue -to read final reading value in meter

ii)cal:-

unit =  finalvalue - invalue


service_charge = total_amount*0.07
(or)
service_charge = total_amount+0.07
net_amount = total_amount + service_charge
'''
invalue = float(input("enter the intial value entered in meter :"))
finalvalue = float(input("enter the final value displayed in meter :"))
units = finalvalue - invalue
print("units used : ",units)
if(units >= 1000):
    total_amount = 9.80
    print("total amount : ",total_amount)
elif(units >= 700):
    total_amount = 8.00
    print("total amount : ",total_amount)
elif(units >= 500):
    total_amount = 6.30
    print("total amount : ",total_amount)
elif(units >= 350):
    total_amount = 5.50
    print("total amount : ",total_amount)
elif(units >= 200):
    total_amount = 3.50
    print("total amount : ",total_amount)
elif(units >= 100):
    total_amount = 1.85
    print("total amount : ",total_amount)
elif(units < 100):
    total_amount = 0.95
    print("total amount : ",total_amount)

service_charge = total_amount*0.07
net_amount = total_amount + service_charge
print("service charge : ",service_charge)
print("net amount : ",net_amount)
    