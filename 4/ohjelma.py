file = open("data.txt", "r")

data = file.read().splitlines()


def contains_fully_another(elf1, elf2):
    elf1_range = elf1.split('-')
    elf2_range = elf2.split('-')

    for i in range(0,2):
        elf1_range[i] = int(elf1_range[i])
        elf2_range[i] = int(elf2_range[i])

    len1 = elf1_range[1]-elf1_range[0]
    len2 = elf2_range[1]-elf2_range[0]

    if len1 >= len2:
        bigger = elf1_range
        smaller = elf2_range
    else:
        bigger = elf2_range
        smaller = elf1_range


    if bigger[0] <= smaller[0] and bigger[1] >= smaller[1]:
        print("MATCH")
        return 1
    else:
        return 0 



    

def main():

    totalPoints = 0
    for x in data:

        pairs = x.split(',')
        print(pairs)
        totalPoints = totalPoints + contains_fully_another(pairs[0], pairs[1])   


    print("sum:", totalPoints)



if __name__ == "__main__":
    main()


