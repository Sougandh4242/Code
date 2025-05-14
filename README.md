Secret Message Encoder and Decoder
This Python project allows users to encode and decode secret messages with a touch of randomness and encryption.

Encoding:

Takes each word from the input message.

Moves the first letter to the end.

Adds 3 random characters at the beginning and the end.

Short words (less than 3 characters) are simply reversed.

Decoding:

Strips away the 3 random characters from both sides.

Moves the last character back to the front to restore the original word.

Words that were reversed are flipped back to normal.
