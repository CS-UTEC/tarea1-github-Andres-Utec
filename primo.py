from math import sqrt, ceil

value = int(input("Ingrese un número: "))
last_value = ceil(sqrt(value))
is_prime = True

prime_list = []
if(value > 2):
    for i in range(2,last_value+1):
        count = 0
        for j in range(2,i+1):
            if(i%j == 0):
                count +=1
            if(count==2):
                break
        if(count == 1):
            prime_list.append(i)
else:
    is_prime = False


for prime_n in prime_list:
    if((value % prime_n) == 0):
        is_prime = False
        break

if((is_prime and (value > 1)) or (value==2)):
    print("The number ", value, " is a prime number")
else:
    print("It's not prime")
