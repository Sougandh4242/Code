# coding and decoding of a secret word
import random
import string

# Take input from the user
words = input("Enter message : ").split()  # Split the message into individual words
option = input("Press 1 for Coding  \nPress 2 for Decoding \n ")

if option == '1':
    # **Coding**
    print("Your Secret code:")
    for word in words:
        length = len(word)  # Calculate length for each word individually

        if length >= 3:
            modified_word = word[1:] + word[0]
            secret_first = ''.join(random.choices(string.ascii_letters + string.digits, k=3))
            secret_second = ''.join(random.choices(string.ascii_letters + string.digits, k=3))
            generated_word = secret_first + modified_word + secret_second
            print(generated_word, end=" ")
        else:
            print(word[::-1], end=" ")

elif option == '2':
    # **Decoding**
    print("Decoded message:")
    for word in words:
        length = len(word)  # Calculate length for each word individually
        
        if length > 6:  # It should have at least 7 characters to be valid
            # Remove the 3-character prefix and suffix
            new = word[3:-3]

            # Move the last character back to the start
            decoded_word = new[-1] + new[:-1]
            print(decoded_word, end=" ")
        else:
            print(word[::-1], end=" ")

else:
    print("Invalid input")
