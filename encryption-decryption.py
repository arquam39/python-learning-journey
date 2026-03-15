#  encryption and decryption

msg = input("emter your msg: ")
words = msg.split(" ")
is_encrept = int(input("Enter 1 for encreption and 2 for decreption :  "))

if is_encrept == 1:
    for word in words:
        if len(word) >= 3:
            import random
            import string
            def get_random_string(length):
                letters = string.ascii_lowercase
                result_st = ''.join(random.choice(letters) for i in range(length))
                return result_st

            r1 = get_random_string(4)
            r2 = get_random_string(4)
            msgnew = r1 + word[1:] + word[0] + r2 
            print(msgnew , end=" ")
        else:
            msgnew = word[::-1] 
            print(msgnew , end=" ")

elif is_encrept == 2:
    for word in words:
       if len(word) >= 3:
           msgnew = word[-5] + word[4:-5] 
           print(msgnew , end=" ")
       else:
           msgnew = word[::-1] 
           print(msgnew , end=" ")

else:
    print("invalid input !")
