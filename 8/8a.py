
file = open("data.txt", "r")

data = file.read().splitlines()

ROWLEN = len(data[0])

dataMatrix = [[] for i in range(ROWLEN)]


def checkVisible(x, y):
    
    blockedCount = 0
    
    for i in range(0, x):
        if dataMatrix[i][y] >= dataMatrix[x][y]:
            blockedCount += 1
            break

    for i in range(x+1, ROWLEN):
        if dataMatrix[i][y] >= dataMatrix[x][y]:
            blockedCount += 1
            break

    for i in range(0, y):
        if dataMatrix[x][i] >= dataMatrix[x][y]:
            blockedCount += 1
            break

    for i in range(y+1, ROWLEN):
        if dataMatrix[x][i] >= dataMatrix[x][y]:
            blockedCount += 1
            break

    if blockedCount < 4:
        return True
    else:
        return False
    

def main():
 
    rowCount = 0
    for row in data:
        for i in range(0,ROWLEN):
            dataMatrix[rowCount].append(int(row[i]))
        rowCount += 1

    visibleCount = 0

    for i in range(1, ROWLEN-1):
        for j in range(1, ROWLEN-1):
            if checkVisible(i,j):
                visibleCount += 1
                #print(i, " ", j, " visible")

    print("Visible inside:", visibleCount)
    visibleCount += 4*(ROWLEN-1) 

    print("Visible:", visibleCount)


if __name__ == "__main__":
    main()


