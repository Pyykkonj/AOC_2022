file = open("data.txt", "r")

data = file.read().splitlines()


def get_char_priority(char):

    asciiNum = ord(char)

    if asciiNum < 97:
        return asciiNum - 38
    else:
        return asciiNum - 96

def get_matching_item(comp1, comp2, comp3):

    print(comp1)
    print(comp2)
    print(comp3)
    

    for i in comp1:
        for j in comp2:
            for k in comp3:
                if i == j == k:
                    print(i)
                    print('')
                    return i
    

def main():

    totalPoints = 0
    groupCounter = 0

    elf1 = ''
    elf2 = ''
    elf3 = ''

    for x in data:

        if groupCounter == 0:
            elf1 = x
            groupCounter = groupCounter + 1
        elif groupCounter == 1:
            elf2 = x
            groupCounter = groupCounter + 1
        elif groupCounter == 2:
            elf3 = x
            mathingItem = get_matching_item(elf1, elf2, elf3)
            totalPoints = totalPoints + get_char_priority(mathingItem)
            groupCounter = 0


    print("sum:", totalPoints)



if __name__ == "__main__":
    main()


