n = []
while True:
    num = int(input("Enter an integer (enter 0 to stop): "))
    if num == 0:
        break
    n.append(num)
print(n)
n.sort()
print("Sorted list of values:")
for num in n:
    print(num)
