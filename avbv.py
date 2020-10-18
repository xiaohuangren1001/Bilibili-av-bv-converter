table = ['f', 'Z', 'o', 'd', 'R', '9', 'X', 'Q', 'D', 'S', 'U', 'm', '2', '1', 'y', 'C', 'k', 'r', '6', 'z', 'B', 'q', 'i', 'v', 'e', 'Y', 'a', 'h', '8', 'b', 't', '4', 'x', 's', 'W', 'p', 'H', 'n', 'J', 'E', '7', 'j', 'L', '5', 'V', 'G', '3', 'g', 'u', 'M', 'T', 'K', 'N', 'P', 'A', 'w', 'c', 'F']
table2 = {'1': 13, '2': 12, '3': 46, '4': 31, '5': 43, '6': 18, '7': 40, '8': 28, '9': 5, 'A': 54, 'B': 20, 'C': 15, 'D': 8, 'E': 39, 'F': 57, 'G': 45, 'H': 36, 'J': 38, 'K': 51, 'L': 42, 'M': 49, 'N': 52, 'P': 53, 'Q': 7, 'R': 4, 'S': 9, 'T': 50, 'U': 10, 'V': 44, 'W': 34, 'X': 6, 'Y': 25, 'Z': 1, 'a': 26, 'b': 29, 'c': 56, 'd': 3, 'e': 24, 'f': 0, 'g': 47, 'h': 27, 'i': 22, 'j': 41, 'k': 16, 'm': 11, 'n': 37, 'o': 2, 'p': 35, 'q': 21, 'r': 17, 's': 33, 't': 30, 'u': 48, 'v': 23, 'w': 55, 'x': 32, 'y': 14, 'z': 19}
def av2bv(avid):
    avid = avid[2:]
    avid = int(avid)
    c = 177451812
    r = avid ^ c
    c2 = 100618342136696320
    r = r + c2
    y = []
    for i in range(10):
        p = pow(58, i)
        p1 = r // p
        y0 = p1 % 58
        y.append(y0)
    ans = []
    for i in y:
        ans.append(table[i])
    rand = [11, 10, 3, 8, 4, 6, 2, 9, 5, 7]
    pair = list(zip(rand, ans))
    pair.sort()
    ans = ['B', 'V']
    for z in pair:
        ans.append(z[1])
    ans = ''.join(ans)
    return ans

def bv2av(bvid):
    bvid = bvid[2:]
    bvid = list(bvid)
    bvid2 = []
    for i in bvid:
        i = table2[i]
        bvid2.append(i)
    bvid = [0] * 10
    bvid[0] = bvid2[0] * pow(58, 6)
    bvid[1] = bvid2[1] * pow(58, 2)
    bvid[2] = bvid2[2] * pow(58, 4)
    bvid[3] = bvid2[3] * pow(58, 8)
    bvid[4] = bvid2[4] * pow(58, 5)
    bvid[5] = bvid2[5] * pow(58, 9)
    bvid[6] = bvid2[6] * pow(58, 3)
    bvid[7] = bvid2[7] * pow(58, 7)
    bvid[8] = bvid2[8] * 58
    bvid[9] = bvid2[9]
    r = sum(bvid)
    r = r - 100618342136696320
    r = r ^ 177451812
    if r < 0: raise TypeError('Illegal bvid')
    r = str(r)
    return 'av' + r
