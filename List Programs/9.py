l = ["January 2023", "February 2024", "March 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
for i in range(len(l)):
    if "2024" in l[i]:
        l[i]=l[i].replace("2024","2023")
    elif "2025" in l[i]:
        l[i]=l[i].replace("2025","2023")
print(l)
        
        
