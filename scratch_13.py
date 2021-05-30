def merge(left, right):
    l = []
    while (len(left) > 0 and len(right) > 0):
        if left[0] < right[0]:
            l.append(left[0])
            left.pop(0)
        else:
            l.append(right[0])
            right.pop(0)
    for i in left:
        l.append(i)
    for i in right:
        l.append(i)
    return l


def sort(block_size, n, a):
    i = 0
    blocks = []
    while (i < n):
        x = a[i:i + block_size]
        i += block_size
        x.sort()
        blocks.append(x)

    res = final_res = []
    for i in blocks:
        k = res
        res = merge(res[:], i[:])
        final_res.append([k[:], i[:], res[:]])
    return res, blocks, final_res


x = list(map(int, raw_input("Enter elements separated by spaces: ").strip().split(" ")))
print()
block_size = int(raw_input("Enter memory blocks size: "))

res, blocks, final_res = sort(block_size, len(x), x)

print("\n----------Sorting Blocks----------\n")
print("The number of blocks is:", len(blocks))
for i, j in enumerate(blocks):
    print("Block {}:  {}".format(i + 1, j))

print("\n----------Merging Passes----------\n")
j = 1
for i in final_res:
    print('Pass {} :   {}'.format(j, i[2]))
    j += 1
