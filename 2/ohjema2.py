file = open("data.txt", "r")

data = file.read().splitlines()

you_points_win = {'A':2, 'B':3, 'C':1}
you_points_lose = {'A':3, 'B':1, 'C':2}
you_points_draw ={'A':1, 'B':2, 'C':3}

def calc_points(you, opponent):

    points = 0
    if( 'X' == you):
        points = 0 + you_points_lose.get(opponent)
    elif( 'Z' == you):
        points = 6 + you_points_win.get(opponent)
    elif( 'Y' == you):
        points = 3 + you_points_draw.get(opponent)

    return points


def main():
    totalPoints = 0
    for x in data:
        totalPoints = totalPoints + calc_points(x[2], x[0])

    print("sum:", totalPoints)


if __name__ == "__main__":
    main()


