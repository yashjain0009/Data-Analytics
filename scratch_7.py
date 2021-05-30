def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

p1 = int(input('Enter the value of p1 = '))
q1 = int(input('Enter the value of q1 = '))
p2 = int(input('Enter the value of p2 = '))
q2 = int(input('Enter the value of q2 = '))


n1 = p1 * q1
t1 = (p1 - 1) * (q1 - 1)

n2 = p2 * q2
t2 = (p2 - 1) * (q2 - 1)

for e1 in range(2, t1):
    if gcd(e1, t1) == 1:
        break

for e2 in range(2, t2):
    if gcd(e2, t2) == 1:
        break

for i in range(1, 10):
    x = 1 + (i*t1)
    if x % e1 == 0:
        d1 = int(x/e1)
        break

for i in range(1, 10):
    x = 1 + (i*t2)
    if x % e2 == 0:
        d2 = int(x/e2)
        break

print('n1 = ' + str(n1) + ' t1 = ' + str(t1) + ' d1 = ' + str(d1) + ' ( ' + str(e1) + ' , ' + str(n1) + ' ) <--- For Sender')
print('n2 = ' + str(n2) + ' t2 = ' + str(t2) + ' d2 = ' + str(d2) + ' ( ' + str(e2) + ' , ' + str(n2) + ' ) <--- For Receiver')

plaintext = input('Plain Text: ')
plaintext = plaintext.upper()


print('Encryption:')
ciphert = []
D1 = []
S = []
for character in plaintext:
    m = ord(character) - 64
    ctt = (m**e2) % n2
    ciphert.append(ctt)
    m = m + 5
    s = (m**d1) % n1
    D1.append(m)
    S.append(s)
print(ciphert)


print('Decryption:')
plaint = []
for i in ciphert:
    dt = (i**d2)
    m = dt % n2
    m = m + 64
    dtt = chr(m)
    plaint.append(dtt)
plaint = ''.join(map(str, plaint))
print(str(plaint))

D2=[]
for i in S:
    m = (i**e1) % n1
    D2.append(m)


print('Verification Of Digital Signature :')
if D1 == D2:
    print("Signature Is Verified")
else:
    print("Signature Is Not Verified")