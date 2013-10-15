Encryption1
===========

Encryption/Decryption Python program

This simple program will take a text file and run it through some fairly simple algorithms to change ASCII values of certain characters, reverse and flip "random" letters and words, etc, etc.
If you don't want to make a seed, you can just enter "n" when you run "encryptor4.py", and it will generate a seed for you. The seed that you enter can be any kind of character, as it will simply take the ASCII value of the string entered as a seed.
After the encryption is done, it will encrypt the output string with the zlib and base64 modules before writing to a file.

I am currently working on making the program insert randomly generated characters throughout the code, at intervals based on the seed. I also hope to have the code run through an RSA encryption.

This is by no means a program to encrypt sensitive information (yet), but it is a nice little program to have to encrypt some plaintext files against the casual user.

