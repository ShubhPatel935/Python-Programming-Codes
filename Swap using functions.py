a=int(input("Enter the 1st value="))
b=int(input("Enter the 2nd value="))

print("values before swapping are")
print(f"a={a}")
print(f"b={b}")

def swapping(a,b):
    tmp=a
    a=b
    b=tmp

    print("Values after swapping are:")
    print(f"a={a}")
    print(f"b={b}")

swapping(a,b)