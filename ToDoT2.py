List =[]

a=int(input("enter the number of To-Do list items : "))

def add():
    for i in range(a):
        b=str(input("enter To-Do list items : "))
        List.append(b)

def view():
    print("original",List)

def remove():
    c=str(input("enter the item to remove : "))
    
    if c in List:
        List.remove(c)
    else:
        print("Not found")
       
          
          

         
add()
view()
remove()
view()
x=str(List)

with open("file.txt", "w") as f:
    for item in List:
        f.write(item + "\n")


with open("file.txt") as f:
    print("File contents:\n" + f.read())

