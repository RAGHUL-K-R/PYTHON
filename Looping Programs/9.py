n=0
e=0
o=0
while n!=-1:
    n=int(input("Enter a number: "))
    if (n%2==0):
        e=e+1
    else:
        o=o+1

print("Number of Even Numbers Entered",e)
print("Number of Odd Numbers Entered",o-1)
