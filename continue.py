#use of continue statement
for i in range(1,101):
    if i%3==0 or i%5==0:
       continue # we want to just skip those values those are divisible by 3
    print(i)

