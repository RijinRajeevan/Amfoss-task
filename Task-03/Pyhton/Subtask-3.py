n=int(input("enter number of rows"))
x=int(n/2+0.5) 
for i in range(1,x+1): # first half 
    for j in range((n-i)-2):   # spaces
        print(" ",end="")
    for j in range(1,2*i):   #stars   
        print("*",end="")
    print() #next line after each row
for i in range(x-1,0,-1): #2nd half
    
    for j in range((n-i)-2):   
        print(" ",end="")
    for j in range(1,2*i):      
        print("*",end="")
    print()