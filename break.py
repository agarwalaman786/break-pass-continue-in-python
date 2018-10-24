av=5 #available candies in the machine
x= int (input("Enter the number of candies you want"))
i=1
while i<=x: #looping system in python
  if i>av: # if values of i is greater than the available candies then machine wll say out of stock
     print ("Out of stock")
     break
  print("candy")
  i+=1

