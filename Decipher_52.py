import string

alphabets = string.ascii_letters

plain_txt = raw_input("Enter a text :")
roll_no = int(input("Enter roll_no :"))
dict1 = {}

cipher = []
prime_no = 5
if roll_no % prime_no == 0:
    key = prime_no
else:
    key = roll_no % prime_no

if key >= 26:
    key = key % 26

for i in range(len(alphabets)):
    dict1[alphabets[i]] = alphabets[(i + key) % len(alphabets)]

for c in plain_txt:
    if c in alphabets:
        temp = dict1[c]
        cipher.append(temp)
cipher = "".join(cipher)
print("cipher text is:", cipher)
print("key is :", key)

dict2 = {}
for i in range(len(alphabets)):
    dict2[alphabets[i]] = alphabets[(i - key) % (len(alphabets))]

decrypt_txt = []

for char in cipher:
    if char in alphabets:
        temp = dict2[char]
        decrypt_txt.append(temp)
    else:
        temp = char
        decrypt_txt.append(temp)

decrypt_txt = "".join(decrypt_txt)
print("decrypted plain_text :", decrypt_txt)