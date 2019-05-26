def listToString(list):
    s = [str(i) for i in list]
    res = "".join(s)

    return(res)


def listToInt(list):
    s = [str(i) for i in list]
    res = int("".join(s))

    return(res)


def stringToBitList(string):
    bitList = [int(i) for i in list(string)]
    return bitList


def convertToBitList(number):

    bitList = []
    tmp = abs(number)

    while tmp != 0:
        bit = tmp % 2
        tmp = tmp//2

        bitList.insert(0, bit)

    while len(bitList) % 8 != 0:
        bitList.insert(0, 0)

    return bitList


def fromDecimal(number):

    if(number >= 0):
        return listToString(convertToBitList(number))
    else:
        power = 8
        maxNumber = 2 ** power
        while(abs(number) > maxNumber):
            power += 8
            maxNumber = 2 ** power

        return listToString(convertToBitList(maxNumber + number))


def toDecimal(number):
    bitList = stringToBitList(number)
    decimalNumber = 0
    power = 0
    while bitList:
        bit = bitList.pop()
        if len(bitList) == 0:
            decimalNumber += (bit * ((-2) ** power))
        else:
            decimalNumber += (bit * (2 ** power))
        power += 1

    return decimalNumber
