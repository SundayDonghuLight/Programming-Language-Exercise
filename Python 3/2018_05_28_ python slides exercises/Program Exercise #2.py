# Exercise[1]:

n1, n2, n3 = input("Enter three different numbers: ").split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
if( n1>=n2 and n1>=n3 ):
    print("%.2f is the largest number." %(n1))
if( n2>=n1 and n2>=n3 ):
    print("%.2f is the largest number." %(n2))
if( n3>=n1 and n3>=n2 ):
    print("%.2f is the largest number." %(n3))


# Exercise[2]:

rows = input("Enter number of rows: ")
rows = int(rows)
for i in range(1,rows+1):
    for j in range(1,i+1):
        print("*", end=" ")
    print("\n", end="")


# Exercise[3]:

def addNumbers(a, b):
    result = a + b
    return result
n1, n2 = input("Enter two numbers: ").split()
n1 = int(n1)
n2 = int(n2)
sum = addNumbers(n1, n2)
print(sum)
