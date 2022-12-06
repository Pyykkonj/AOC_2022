file = open("data.txt", "r")


numRead = []

def check_distinctity():

    alphabets = list("abcdefghijklmnopqrstuvwxyz")

    for i in range(0,len(numRead)):
        char = ord(numRead[i])-97
        if alphabets[char] == chr(char+97):
            alphabets[char] = ' '
        else:
            return -1

    return 0

def check_start(num):
    numRead.append(num)

    if len(numRead) < 14:
        return -1
    elif len(numRead) == 15:
        numRead.pop(0)
    
    return check_distinctity()
    


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


