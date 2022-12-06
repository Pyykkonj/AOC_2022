file = open("data.txt", "r")

data = file.read().splitlines()

#print(data)


you_points = {'X':1, 'Y':2, 'Z':3}

you_win = {'X':'C', 'Y':'A', 'Z':'B'}

equal = {'X':'A', 'Y':'B', 'Z':'C'}

def calc_points(you, opponent):

    print("you", you)
    print("Op", opponent)
    points = 0
    if(you_win.get(you) == opponent):
        points = 6
    elif(equal.get(you) == opponent):
        points = 3
    else:
        points = 0

   # print(you_points.get(you))

    points = points + you_points.get(you)

    print("points", points)

    return points



def main():
    totalPoints = 0
    for x in data:
        print(x)
        totalPoints = totalPoints + calc_points(x[2], x[0])


    print("sum:", totalPoints)



if __name__ == "__main__":
    main()


