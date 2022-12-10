
file = open("data.txt", "r")

data = file.read().splitlines()



def main():

    x = 1
    cycleNumber = 1
    signalStrength = 0
    signalStrengthSum = 0

    cmds = ""
    readCommand = True

    pc = 0

    while pc != len(data):   
        #print(cycleNumber, " ", x)

        if (cycleNumber == 20) or ((cycleNumber%40)-20 == 0):
            signalStrength = cycleNumber * x
            signalStrengthSum += signalStrength
            #print("cycle: ", cycleNumber, " x: ", x, " ss: ", signalStrength)

        if readCommand == True:
            cmds = data[pc].split(" ")

            if cmds[0] == "noop":
                readCommand = True

            elif cmds[0] == "addx":
                readCommand = False
            
            pc += 1
        else:
            x += int(cmds[1])
            readCommand = True
        
        cycleNumber += 1


    print("\nfinalSum", signalStrengthSum)

            



if __name__ == "__main__":
    main()


