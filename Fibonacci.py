# To print fibonacci

n=int(input("Enter the Number="))

a=0
b=1
sum=a+b

print(a)
print(b)
for i in range(0,n):
    print(sum)
    a=b
    b=sum
    sum=a+b