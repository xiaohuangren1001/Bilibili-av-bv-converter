TABLE = ['f', 'Z', 'o', 'd', 'R', '9', 'X', 'Q', 'D', 'S', 'U', 'm', '2', '1', 'y', 'C', 'k', 'r', '6', 'z', 'B', 'q', 'i', 'v', 'e', 'Y', 'a', 'h', '8', 'b', 't', '4', 'x', 's', 'W', 'p', 'H', 'n', 'J', 'E', '7', 'j', 'L', '5', 'V', 'G', '3', 'g', 'u', 'M', 'T', 'K', 'N', 'P', 'A', 'w', 'c', 'F']
REV_TABLE = { "F": 0, "c": 1, "w": 2, "A": 3, "P": 4, "N": 5, "K": 6, "T": 7, "M": 8, "u": 9, "g": 10, "3": 11, "G": 12, "V": 13, "5": 14, "L": 15, "j": 16, "7": 17, "E": 18, "J": 19, "n": 20, "H": 21, "p": 22, "W": 23, "s": 24, "x": 25, "4": 26, "t": 27, "b": 28, "8": 29, "h": 30, "a": 31, "Y": 32, "e": 33, "v": 34, "i": 35, "q": 36, "B": 37, "z": 38, "6": 39, "r": 40, "k": 41, "C": 42, "y": 43, "1": 44, "2": 45, "m": 46, "U": 47, "S": 48, "D": 49, "Q": 50, "X": 51, "9": 52, "R": 53, "d": 54, "o": 55, "Z": 56, "f": 57, }

MAX_AVID = 1 << 51
MIN_AVID = 1

def av2bv(avid: str):
    if not avid.lower().startswith('av'):
        raise TypeError('invalid avid format')
    avid = avid[2:]
    avid = int(avid)
    if avid <= MIN_AVID:
        raise TypeError('avid too small')
    if avid >= MAX_AVID:
        raise TypeError('avid too big')
    c = 23442827791579
    c2 = 2251799813685247
    r = MAX_AVID | avid
    r ^= c
    y = []
    for i in range(10):
        p = pow(58, i)
        p1 = r // p
        y0 = p1 % 58
        y.append(y0)
    ans = []
    for i in y:
        ans.append(TABLE[i])
    rand = [11, 10, 3, 8, 4, 6, 2, 9, 5, 7]
    pair = list(zip(rand, ans))
    pair.sort()
    ans = ['B', 'V']
    for z in pair:
        ans.append(z[1])
    ans = ''.join(ans)
    return ans

def bv2av(bvid: str):
    if not bvid.lower().startswith("bv1"):
        raise TypeError('Illegal bvid')

    bvid_list: list[str] = list(bvid[3:])
    swap(bvid_list, 1, 4)
    swap(bvid_list, 0, 6)

    avid = 0
    for byte in bvid_list:
        index = REV_TABLE.get(byte, None)
        if index is None:
            raise TypeError('bvid contains illegal character')
        avid *= 58
        avid += index

    avid &= 2251799813685247
    avid ^= 23442827791579
    if avid < 0: raise TypeError('Illegal bvid')
    avid = str(avid)
    return 'av' + avid

def swap(list: list, index1: int, index2: int):
    temp = list[index2]
    list[index2] = list[index1]
    list[index1] = temp
