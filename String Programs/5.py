str1=input("enter email:")
str2=""
for i in str1:
    if(i=='@'):
        break
    else:
        str2+=i
str3=str2[::-1]
print(str2)
str3=str.lower(str3)
print(str2+str3)
