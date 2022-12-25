file_handle=open("Krenil.txt",'w')
name=input("Enter the name=")
age=input("Enter the age=")
DOB=input("Enter the DOB=")

file_handle.write("-> Krenil is Great <-"+"\n")

file_handle.write(name+"\n")
file_handle.write(age+"\n")
file_handle.write(DOB+"\n")

file_handle.close()

file_handle=open("Krenil.txt","r")
print("1st Line=",file_handle.readline())
print("2nd Line=",file_handle.readline())
print("3rd Line=",file_handle.readline())
print("4th Line=",file_handle.readline())

print("Mode of the file=",file_handle.mode)
print("Name of the file=",file_handle.name)