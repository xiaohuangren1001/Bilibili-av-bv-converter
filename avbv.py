TABLE = [
  'F', 'c', 'w', 'A', 'P', 'N', 'K', 'T', 'M', 'u', 'g', '3', 'G', 'V', '5', 'L',
  'j', '7', 'E', 'J', 'n', 'H', 'p', 'W', 's', 'x', '4', 't', 'b', '8', 'h', 'a',
  'Y', 'e', 'v', 'i', 'q', 'B', 'z', '6', 'r', 'k', 'C', 'y', '1', '2', 'm', 'U',
  'S', 'D', 'Q', 'X', '9', 'R', 'd', 'o', 'Z', 'f',
]
REV_TABLE = { "F": 0, "c": 1, "w": 2, "A": 3, "P": 4, "N": 5, "K": 6, "T": 7,
              "M": 8, "u": 9, "g": 10, "3": 11, "G": 12, "V": 13, "5": 14, "L": 15,
              "j": 16, "7": 17, "E": 18, "J": 19, "n": 20, "H": 21, "p": 22, "W": 23,
              "s": 24, "x": 25, "4": 26, "t": 27, "b": 28, "8": 29, "h": 30, "a": 31,
              "Y": 32, "e": 33, "v": 34, "i": 35, "q": 36, "B": 37, "z": 38, "6": 39,
              "r": 40, "k": 41, "C": 42, "y": 43, "1": 44, "2": 45, "m": 46, "U": 47,
              "S": 48, "D": 49, "Q": 50, "X": 51, "9": 52, "R": 53, "d": 54, "o": 55,
              "Z": 56, "f": 57, }

MAX_AVID = 1 << 51
MIN_AVID = 1

XOR_CODE = 23442827791579
MASK_CODE = 2251799813685247
BASE = 58

def av2bv(avid: str):
    if not avid.lower().startswith('av'):
        raise TypeError('invalid avid format')
    avid_num = int(avid[2:])
    if avid_num < MIN_AVID:
        raise TypeError('avid too small')
    if avid_num >= MAX_AVID:
        raise TypeError('avid too big')

    r = MAX_AVID | avid_num
    r ^= XOR_CODE
    
    ans = ['B', 'V', '1'] + ['0']*9
    bvidx = len(ans) - 1

    while r:
        idx = r % BASE
        code = TABLE[idx]
        ans[bvidx] = code
        r //= BASE
        bvidx -= 1

    swap(ans, 3, 9)
    swap(ans, 4, 7)

    return ''.join(ans)

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
        avid *= BASE
        avid += index

    avid &= MASK_CODE
    avid ^= XOR_CODE
    if avid < 0: raise TypeError('Illegal bvid')
    avid = str(avid)
    return 'av' + avid

def swap(list: list, index1: int, index2: int):
    temp = list[index2]
    list[index2] = list[index1]
    list[index1] = temp