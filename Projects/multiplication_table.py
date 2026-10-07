#Eh p1 multiplication table

print("Multiplication Chart 1-12")
print()

print("x", end="\t")
for i in range(1, 13):
    print(i, end="\t")
print()

for i in range(1, 13):
    print(i, end="\t")          
    for j in range(1, 13):
        print(i * j, end="\t")  
    print()                     

