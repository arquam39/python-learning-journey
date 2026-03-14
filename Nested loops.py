# check prime number using for loop

number = int(input("eneter a number : "))

if number > 1:
    for i in range(2,number):
        if number % i == 0:
            print(f"{number} is a not prime number ")
            break
    else:
        print(f"{number} is a prime number ")
else:
    print(f"{number} is a not prime number ")



# check prime number using while loop

number = int(input("eneter a number : "))
i = 2
is_prime = True
if number > 1:
    while i < number:
        if number % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(f"{number} is a prime number ")
    else:
        print(f"{number} is a not prime number ")
else:
    print(f"{number} is not a prime number ")



# # check prime number usong for loop

num = int(input("enter:"))
i = 2
is_prime = True
if num > 1:
    while i < num:
        if num %i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print("yes")
    else:
        print("Not")

else:
    print("not")