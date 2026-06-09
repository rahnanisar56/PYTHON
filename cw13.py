import os
name= input("Enter the name of the new item:")
if not os.path.exists("items.txt"):
    f=open("items.txt","w")
    f.write(name+"\n")
    f.close()
else:
    f=open("items.txt","a")
    f.write(name+"\n")
    f.close()
    
print("Displaying the full list of Items\n")

f=open("items.txt","r")
print(f.read())
f.close()
    
    
    