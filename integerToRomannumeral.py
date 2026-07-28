# // I = 1
# // V = 5
# // X = 10
# // L = 50
# // C = 100
# // D = 500
# // M = 1000
# // 4999 is max integer that can be represented without vinculum
# // 0 is nulla (N)
# // int and roman numeral inputs will be 1 to 4999 and I to MMMMCMXCIX

# // 3749
# // MMMDCCXLIX

import re


def converter(rn: str, idx: int):
    one = "I"
    five = "V"
    ten = "X"
    fifty = "L"
    onehundred = "C"
    fivehundred = "D"
    millenium = "M"

    single = one
    middle = five
    next = ten
    if idx == 1:
        # tens
        single = ten
        middle = fifty
        next = onehundred
    elif idx == 2:
        # hundreds
        single = onehundred
        middle = fivehundred
        next = millenium
    elif idx == 3:
        # thousands
        single = millenium

    result = rn.replace("Sin", single).replace("Mid", middle).replace("Next", next)
    return result


def abstracter(elem: int, idx: int):
    rn = ""
    for pointer in range(1, elem + 1):
        if pointer == 4:
            if idx == 3:
                rn = "SinSinSinSin"
            else:
                rn = "SinMid"
        elif pointer == 5:
            rn = "Mid"
        elif pointer == 9:
            rn = "SinNext"
        else:
            rn = rn + "Sin"

    result = converter(rn, idx)
    return result


def intToRn(intInput: int):
    rnStr = str(intInput)
    rnList = list(rnStr)
    rnList.reverse()

    rnOutput = []

    for index, rnDigit in enumerate(rnList):
        rnOutput.insert(index, abstracter(int(rnDigit), index))

    rnOutput.reverse()
    result = "".join(rnOutput)
    print(result)

    return result


intToRn(793)
# MMMMDCXLIII
