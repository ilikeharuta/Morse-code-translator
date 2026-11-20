from morse import morselibrary
import winsound
import time

input2 = input("enter a string")
new_list = list(input2)
listlength = len(new_list)
compile2 = []
estring = ""


for a in new_list:
   for b in morselibrary:
       if a == b:
           estring += morselibrary[b]
           compile2.append(morselibrary[b])


print(estring)
for i in estring:
    time.sleep(0.35)
    if i == ".":
        winsound.Beep(600,200)
    elif i == "_":
        winsound.Beep(600,500)
    else:
        time.sleep(0.25)