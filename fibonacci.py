# program to print the first 50 fibonacci numbers
N=int(input("How many numbers you want to printthe fibonnaci series")) 
a=0
b=1
print(a)
print(b)
for i in range(0,(N-2)):
    c=a+b
    print(c)
    a=b
    b=c

    
