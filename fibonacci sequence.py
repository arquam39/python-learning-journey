# fibonacci sequence by for loop
a = 0
b = 1

for i in range (12):
    print(a, end=" ")
    next_term = a+b
    a = b
    b = next_term


# fibonacci sequence by while loop
a = 0
b = 1
 
while a <= 100:
     print(a, end=" ")
     next_term = a+b
     a = b
     b = next_term
