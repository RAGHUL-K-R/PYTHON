n=[]
s=int(input("enter the no of words"))
for i in range(s):
    string=input("enter the words")
    n.append(string)
print(n)
for s in n:
    print(f"{s}: {len(s)}")
largest = max(n)
print("longest word:",largest)
