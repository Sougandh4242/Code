# coding and decoding of a secret word
import random
import os
import string
words=input("Enter message : ")
length=len(words)
option=input("Press 1 for Coding  \nPress 2 for Decoding \n ")
if option=='1':
    #coding
    print("Your Secret code")
    for word in words:

        if (length>=3) : 
            modified_word=word[1:]+word[0]
            secret_first=''.join(random.choices(string.ascii_letters+string.digits,k=3))
            secret_second=''.join(random.choices(string.ascii_letters+string.digits,k=3))
            generated_word=secret_first+modified_word+secret_second
            print(generated_word,end=" ")

    else: print(word[::-1])
elif option=='2':
    #Decoding
    for word in words:
       if length > 6:  # It should have at least 7 characters to be valid
            # Remove the 3-character prefix and suffix
            new = word[3:-3]

            # **Check if `new` is not empty** before trying to access
            if len(new) > 0:
                # Move the last character back to the start
                decoded_word = new[-1] + new[:-1]
            else:
                decoded_word = new  # If it's empty, just leave it as is
                
            print(decoded_word, end=" ")
    else: print(word[::-1])

else:print("Invalid input")