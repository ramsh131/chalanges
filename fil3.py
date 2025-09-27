# create a list of first 100 numbers

num = []

for i in range (1, 101) :
    num.append(i)
    print(num)
    
    
    
# create a list for all even numbers and odd numbers

even = []
odd = []

for i in num :
    if i % 2 == 0 :
        even.append (i)
    else:
        odd.append (i) 
            
        print('even numbers are', 'even')
        print('odd numbers are', 'odd')
        
# create a list number that divisibile by both  3 and 5


divisible = []
 
for i in num :
   if  i % 5 == 0 and i % 3 == 0 :
    divisible.append (i)
    print('divisible are','divisible')
       
    
         
        