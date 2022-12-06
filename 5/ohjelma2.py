file = open("data.txt", "r")

data = file.read().splitlines()

# 2D List
crateStack = [[] for i in range(9)]


def printCrateStack():
    for i in crateStack:
        for j in i:
            print(j,  end='')
        print('')


def parse_initial_crate(row):
    crateStackCounter = 0
    for i in range (1, 4*9, 4):
        if row[i] != ' ':
            crateStack[crateStackCounter].append(row[i])
        crateStackCounter = crateStackCounter + 1

def move_crate(row):

    row_array = row.split(' ')

    print(row_array)

    crate_nbr = int(row_array[1])
    crate_from = int(row_array[3]) - 1
    crate_to = int(row_array[5]) - 1      

    temp = []

    for i in range(0, crate_nbr):
        crate = crateStack[crate_from].pop()
        temp.append(crate)

    temp.reverse()
    crateStack[crate_to].extend(temp)
    
    #printCrateStack()



def main():

    printCrateStack()
    initialStackRead = False

    
    for x in data:

        if x == '':
            initialStackRead = True
            for i in crateStack:
                i.reverse()
            printCrateStack()
            continue

        if initialStackRead == False:
            parse_initial_crate(x)
        else:
            move_crate(x)


        
    printCrateStack()

    for i in crateStack:
        print(i.pop(), end='')




if __name__ == "__main__":
    main()


