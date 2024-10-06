''' write a program to generate only even number between 5 to n 
number. '''

n=int(input("enter the range to print : "))
i=5
while(i<=n):
  if i%2==0 :
       print(i)
  i=i+1
