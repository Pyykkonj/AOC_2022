
file = open("data.txt", "r")

data = file.read().splitlines()

ROWLEN = len(data[0])

dataMatrix = [[] for i in range(ROWLEN)]


def countScenicScore(x, y):
    
    a=0
    b=0
    c=0
    d=0
    
    for i in reversed(range(0, x)):
        a += 1
        if dataMatrix[i][y] >= dataMatrix[x][y]:
            break

    for i in range(x+1, ROWLEN):
        b += 1
        if dataMatrix[i][y] >= dataMatrix[x][y]:  
            break

    for i in reversed(range(0, y)):
        c += 1
        if dataMatrix[x][i] >= dataMatrix[x][y]:
            break

    for i in range(y+1, ROWLEN):
        d += 1
        if dataMatrix[x][i] >= dataMatrix[x][y]:
            break

    return a*b*c*d
    

def main():
 
    rowCount = 0
    for row in data:
        for i in range(0,ROWLEN):
            dataMatrix[rowCount].append(int(row[i]))
        rowCount += 1

    highersScore = 0

    for i in range(1, ROWLEN-1):
        for j in range(1, ROWLEN-1):
            treeScore = countScenicScore(i,j)
            if treeScore > highersScore:
                highersScore = treeScore
                #print(i, " ", j, " score: ", treeScore)

    print("score:", highersScore)


if __name__ == "__main__":
    main()


