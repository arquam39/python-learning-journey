# printing the elements of a list using indexing
num = [1,4,9,16,25,36,49,64,81,100]
hero = ["superman", "spiderman" ,"batman"]

print(num[0])
print(num[1])
print(num[2])
print(num[3])
print(num[4])
print(num[5])
print(num[6])
print(num[7])
print(num[8])
print(num[9])


# printing the elements of a list using while loop
ind = 0
while ind <= 9: 
    print(num[ind])
    ind += 1
    break


# printing the table of number using while loop

x = int(input("enter :"))
i = 1

while i <= 10:
    print(x,"*",i,"=",x*i)
    i += 1



# printing the elements of a list using while loop

num = (1,4,9,16,25,36,49,64,81,100,36)
x = 4
ind = 0

while ind <= len(num):
    if(num[ind] == x):
        print("found at ordex",ind)
    else:
        print("not found at",ind)
    ind += 1


# printing the elements of a list using for loop

num = (1,4,9,16,25,36,49,64,81,100,36)
x = int(input("search:"))
ind = 0

for val in num:
    if (num[ind] == x):
        print("found at",ind)
        ind += 1
        break
    else :
        print("finding...")
        ind += 1
print("loop ended")



# find the index of x in num

num = (1,4,9,16,25,36,49,64,81,100,36)
x = int(input("search:"))
ind = 0

for val in num:
    if (num[ind] == x):
        print("found at",ind)
        ind += 1
        break
    else :
        print("finding...")
        ind += 1
print("loop ended")