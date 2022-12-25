file_handle=open("Bhai.txt","w")
name=input("Enter name=")
age=input("Enter age=")

file_handle.write("Krenil is great"+"\n")

file_handle.write(name+"\n")
file_handle.write(age+"\n")

file_handle.close()

file_handle=open("Bhai.txt","r")

print("Content in file is=",ile_handle.readline())