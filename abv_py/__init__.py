from abv_py.const import __const
from abv_py.util import swap


def av2bv(avid_num: int) -> str:
    if avid_num < __const.MIN_AVID:
        raise TypeError("avid too small")
    if avid_num >= __const.MAX_AVID:
        raise TypeError("avid too big")

    r = __const.MAX_AVID | avid_num
    r ^= __const.XOR_CODE

    ans = ["B", "V", "1"] + ["0"] * 9
    bvidx = len(ans) - 1

    while r:
        idx = r % __const.BASE
        code = __const.TABLE[idx]
        ans[bvidx] = code
        r //= __const.BASE
        bvidx -= 1

    swap(ans, 3, 9)
    swap(ans, 4, 7)

    return "".join(ans)


def bv2av(bvid: str) -> int:
    if not bvid.lower().startswith("bv1"):
        raise TypeError("Illegal bvid prefix")
    if not len(bvid) == 12:
        raise TypeError("Invalid bvid length")
    for ch in list(bvid):
        if not ch.isascii():
            raise TypeError("bvid should not contain non-ASCII")

    bvid_list: list[str] = list(bvid[3:])
    swap(bvid_list, 1, 4)
    swap(bvid_list, 0, 6)

    avid = 0
    for byte in bvid_list:
        index = __const.REV_TABLE.get(byte, None)
        if index is None:
            raise TypeError(f"bvid contains illegal character {byte}")
        avid *= __const.BASE
        avid += index

    avid &= __const.MASK_CODE
    avid ^= __const.XOR_CODE
    if avid < __const.MIN_AVID or avid >= __const.MAX_AVID:
        raise TypeError(f"Invalid bvid {bvid}")
    return avid
