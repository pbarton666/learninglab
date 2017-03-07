#py_magic_decoder_ring.py


"Using bitwise XOR as a 'quick and dirty magic decoder ring'"

secret=100
key=50
#XOR is simple to apply...
print("An XOR operation using ^ (result is 1 if a single bit is 1)")
print("{:>10} (original) XOR ".format(bin(secret)))
print("{:>10} (the key) yields".format(bin(key)))
print("{:>10} (encrypted result)".format(bin(secret^key)) )
#... and it can be used as an inverse operation.
print()
print("Now, if you re-apply the key to the cipher ...")
print("{:>10} (encrypted result) XOR \n {:>10} (the key)"
      " you get the original back:\n{:>10}"\
      .format(bin(secret^key), 
              bin(key), 
              bin(secret^key^key)))


#get the message and encryption key
print("\nLet's try:")

debug=True
encoding='utf-8'  #128 ASCII characters, used for conversion to bytes

if debug:
    message="Secret Agent 007"
    key=0x41 #"A"
else:	
    message=input("Message to encode: ")
    key=input("What's the encryption key?  ")

#convert the message to bytes (binary) using an array of bytes
encode = bytearray(message, encoding)  
for i in range(len(encode)):
    encode[i] ^=key

print("Original: {}".format(message))	
print("Encrypted:  {}".format(encode))

#this builds a string out of the decrypted characters
decode = ""
for i in range(len(encode)):
    decode+=chr(encode[i] ^key)
print("Back again: ".format(decode))

#An, but beware of the pitfall here
print("Note, though, there's a zero in the message")
print("  in position {}.".format(message.find('0')))
print()
print("If someone knew (or guessed that) our cypher is at risk:")
print("The key: {}   0^key  {}".format(key, 0^key))

for char in message:
    key=bytearray(char, encoding)[0]
    decode = ""
    for i in range(len(encode)):
        decode+=chr(encode[i] ^key)	
    print("Trying key {} ... decrypt is: {}".format(char, decode))

print()
print("So don't try this for anything more important than a Christmas ")
print("   gift list you're keeping from your kids, but have fun!")

