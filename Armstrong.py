a=int(input('enter a number '))
s=0
d=a
while a>0:
    c=a%10
    s=c*c*c+s
    a=a//10
if(s==d):
    
    print(d," is an armstrong number")
else:
    print(d," is not an armstrong number")
