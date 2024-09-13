f1 = open("input.txt","r")
n = int(f1.readline())
f2 = open("output.txt","w")
x=int(n/2+0.5)  
for i in range(1,x+1): # first half 
    f2.write(" " * ((n - i) - 2)) # spaces  
    f2.write("*" * (2 * i - 1))#stars   
    f2.write("\n") #next line after each row
for i in range(x-1,0,-1): #2nd half
    f2.write(" " * ((n - i) - 2)) # spaces  
    f2.write("*" * (2 * i - 1))#stars   
    f2.write("\n") #next line after each row
f1.close()
f2.close()


