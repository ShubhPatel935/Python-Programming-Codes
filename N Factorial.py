# To find N factorial

n=int(input("Enter the value="))

fact=1

if(n<=2):
    print(f"Factorial of {n} is {n}")
else:
    for i in range(1,n+1):
        fact=fact*i

print(f"Factorial of {n} is {fact}")