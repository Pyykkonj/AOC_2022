file = open("data.txt", "r")

data = file.read().splitlines()

#print(data)

max_cals = [0,0,0]


def add_biggest(num):

    global max_cals
    max_cals.sort()

    if num > max_cals[0]:
        max_cals[0] = num
    elif num > max_cals[1]:
        max_cals[1] = num
    elif num > max_cals[2]:
        max_cals[2] = num
    

def main():
    cumulative = 0
    for x in data:
        if x == '':
            add_biggest(cumulative)
            cumulative = 0
        else:
            cumulative = cumulative + int(x)


    print(max_cals[0])
    print(max_cals[1])
    print(max_cals[2])

    print("sum:", max_cals[0]+max_cals[1]+max_cals[2])



if __name__ == "__main__":
    main()


