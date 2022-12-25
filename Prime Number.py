# To check for prime number

n=int(input("Enter the number="))

flag = False #flag is defined in the begining

if(n<=1):
    print("Enter the number greater than 2")
else:
    for i in range(2, n):
        if(n%i==0):
            flag=True
            break


if(flag==True):
    print(f"{n} is not a prime number")
else:
    print(f"{n} is a prime number")