# To check whether the given number is prime or not
x= int(input("Enter the number to check whether it is prime or not"))
i=2
while i<=x:
    if x%i==0:
       break
    i=i+1
if(x==i):
   print("Number is prime")
else:
   print("Number is not prime")
