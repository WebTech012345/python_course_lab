# Initialize the values of a and b
a = 32         
b = 6          

# Perform operations using assignment operators and display results

print('a=b:', a == b)   # Checking if a equals b; this will print 'False'

a = 32  # Reset a to 32
a += b  
print('a+=b:', a)   # a = a + b => a = 32 + 6 => 38

a -= b  
print('a-=b:', a)   # a = a - b => a = 38 - 6 => 32

a *= b  
print('a*=b:', a)   # a = a * b => a = 32 * 6 => 192

a %= b  
print('a%=b:', a)   # a = a % b => a = 192 % 6 => 0 (remainder when dividing 192 by 6)

a = 32  # Reset a to 32 for the next operation
a **= b  
print('a**=b:', a)  # a = a ** b => a = 32 ** 6 => 1073741824

a //= b  
print('a//=b:', a)  # a = a // b => a = 1073741824 // 6 => 178956970 (integer division)
