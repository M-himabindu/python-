n1=int(input("enter the number1:"))
n2=int(input("enter the number2:"))
x=max(n1,n2)
count=0
for i in range(1,x):
    if(n1%i==0 and n2%i==0):
        count+=1
print(count)
prod=(n1*n2)
sum=n1+n2
if (prod%sum==0):
    print("yeah")
else:
    print("nah")
        
