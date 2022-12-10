
file = open("data.txt", "r")

data = file.read().splitlines()

def main():

    x = 1
    cycleNumber = 1


    crt = ""
    cmds = ""
    readCommand = True

    pc = 0

    while pc != len(data):   
        #print(cycleNumber, " ", x, end="")

        if (x-1) <= ((cycleNumber-1)%40) <= (x+1):
            crt += "#"
            #print(" x")
        else:
            crt += "."
            #print(" .")


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



    for i in range(0,len(crt)):
        if (i==0):
            print(crt[i], end="")
        else:
            if (i+1)%40 == 0:
                print(crt[i])
            else:
                print(crt[i], end="")

            



if __name__ == "__main__":
    main()


