list=[]

n=int(input("Enter the number of element="))

for i in range(0,n):
    ele=int(input())
    list.append(ele)

print("List=",list)

print("Biggest element in the list is=",max(list))