X11=str(input(" "))
count=0
for i in X11:
    if i.isnumeric() or i.isalpha():
        pass
    else:
        count+=1
print(count)
