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


def rnToInt(rninput: str):
    rnList = re.split(r"(IV|IX|XL|XC|CD|CM|I|V|X|L|C|D|M)", rninput)
    rnListCleaned = list(filter(None, rnList))
    # rnListCleaned = [rn for rn in rnList if len(rn) > 0]
    print(rnListCleaned)

    rnMap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    rnSummation = 0

    for rnValue in rnListCleaned:
        if len(rnValue) == 2:
            rnSummation -= rnMap[rnValue[0]]
            rnSummation += rnMap[rnValue[1]]
        else:
            rnSummation += rnMap[rnValue]

    print(rnSummation)

    return


rnToInt("MMCDLXXXVI")

# MMCDLXXXVI
# 2486

# MMMDCCXLIX
# 3749
