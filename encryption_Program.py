import random
import string

chars = string.punctuation + string.digits + string.ascii_letters + " "

chars = list(chars)

key = chars.copy()
random.shuffle(key)

plain_txt = input("Enter a message to encrypt : ")
cypher_txt = ""

for letter in plain_txt:
    index = chars.index(letter)
    cypher_txt += key[index]

print("Original message : ",plain_txt)
print(f"Encrypted message : {cypher_txt}")
print("******************************************")
cypher_txt = input("Enter a message to decrypt : ")
plain_txt = ""

for letter in cypher_txt:
    index = key.index(letter)
    plain_txt += chars[index]

print("Encrypted message : ",cypher_txt)
print(f"Original message : {plain_txt}")