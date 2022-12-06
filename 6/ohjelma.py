file = open("data.txt", "r")

numRead = []

def check_start(num):
    numRead.append(num)

    if len(numRead) < 4:
        return -1
    elif len(numRead) == 5:
        numRead.pop(0)

    print(numRead[0], " ", numRead[1] , " ",  numRead[2] , " ",  numRead[3])
    
    if (ord(numRead[0]) - ord(numRead[1])) != 0 and (ord(numRead[2]) - ord(numRead[3])) != 0:
        if (ord(numRead[0]) - ord(numRead[2])) != 0 and (ord(numRead[1]) - ord(numRead[3])) != 0:
            if (ord(numRead[0]) - ord(numRead[3])) != 0 and (ord(numRead[1]) - ord(numRead[2])) != 0:
                return 0
    
    return -1
    


def main():

    startIndex = 0

    while 1:
        x = file.read(1)
        if not x:
            break

        retval = check_start(x)
        startIndex += 1

        if retval == 0:
            break

    print(startIndex)
        




if __name__ == "__main__":
    main()


