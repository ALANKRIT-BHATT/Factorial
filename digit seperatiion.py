x=int(input("Enter a number to sperate it's digits  "))
while x>0:
    y=int(x%10) 
    print(y)
    x=int(x/10)
