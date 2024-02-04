def swap(list: list, index1: int, index2: int):
    temp = list[index2]
    list[index2] = list[index1]
    list[index1] = temp
