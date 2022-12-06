file = open("data.txt", "r")

data = file.read().splitlines()


def get_char_priority(char):

    asciiNum = ord(char)

    if asciiNum < 97:
        return asciiNum - 38
    else:
        return asciiNum - 96

def get_matching_item(comp1, comp2):

    print(comp1)
    print(comp2)
    #print('')

    for i in comp1:
        for j in comp2:
            if i == j:
                return i
    

def main():

    totalPoints = 0
    for x in data:
        strLen = len(x)

        print(x)
        #print("len", strLen)

        half = int(strLen/2)

        mathingItem = get_matching_item(x[0:half], x[half:strLen])

        print(mathingItem)
        print('')

        totalPoints = totalPoints + get_char_priority(mathingItem)



    print("sum:", totalPoints)



if __name__ == "__main__":
    main()


