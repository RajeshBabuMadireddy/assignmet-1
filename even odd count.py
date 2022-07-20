numbers=[]
even=0
odd=0
n=int(input("enter the number of elements"))
for i in range(0,n):
    elements=int(input("enter the elements"))
    numbers.append(elements)
for i in numbers:    
        if i%2==0:
            even=even+1
        else:
            odd=odd+1
        
print("even numbers are :",even)
print("odd numbers are :",odd)         
    