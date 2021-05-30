pl_txt = raw_input("Enter plain text to encrypt: ")
pl_txt = pl_txt.replace(" ", "").lower()
l = len(pl_txt)
print("The length of plain text is",l)
print("Choose a suitable matrix size(m x n) such that m*n >= length of text")
m = int(input("Enter no. of rows: "))
n = int(input("Enter no. of columns: "))
if m*n < l :
    print("Matrix size less than length of text")
    exit()
else:
    rem = "*" * ((m*n) - l)
    pl_txt += rem

pl_mat = []
for i in range(m):
    r = i*n
    temp = list(pl_txt[r : (r+n)])
    pl_mat.append(temp)

for i in pl_mat:
    print(i)

print("Enter row permutation sequence from", 0, "to", m-1)
rp = raw_input()
rowp = [int(x) for x in rp]
rp_mat=[]
for i in rowp:
    rp_mat.append(pl_mat[i])

print("-----After Row Permutation-----")
for i in rp_mat:
    print(i)

print("Enter column permutation sequence from", 0, "to", n-1)
cp = raw_input()
colp = [int(x) for x in cp]
cp_mat=[]
rp_mat = [[rp_mat[j][i] for j in range(m)] for i in range(n)]
for i in colp:
    cp_mat.append(rp_mat[i])
cp_mat = [[cp_mat[j][i] for j in range(n)] for i in range(m)]

print("-----After Column Permutation-----")
for i in cp_mat:
    print(i)

print("----------Encrypting----------")
cp_txt=''
for i in range(m):
    for j in range(n):
        cp_txt+=cp_mat[i][j]
print("The cipher text is ",cp_txt)
