n = input()
x = input().split()
x0 = 0
x1 = 0
x2 = 0
x3 = 0
x4 = 0

for i in x :
    if(int(i)<=20):
        x0+=1
    elif(int(i)<=40):
        x1+=1
    elif(int(i)<=60):
        x2+=1
    elif(int(i)<=80):
        x3+=1
    else:
        x4=x4+1

print(x0)
print(x1)
print(x2)
print(x3)
print(x4)
    
