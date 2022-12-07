file = open("data.txt", "r")

data = file.read().splitlines()



class TreeNode:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.subfolders = []
        self.files = []
        

    def addFile(self, name, size):
        newFile = (name, int(size))
        self.files.append(newFile)

    def addFolder(self, name):
        # Check folder allready exist
        for i in self.subfolders:
            if i.getName() == name:
                return

        newFolder = TreeNode(name, self)
        self.subfolders.append(newFolder)
    
    def getName(self):
        return self.name
    
    def getSubFolder(self, name):
        for i in self.subfolders:
            if i.getName() == name:
                return i

    def getSubFolders(self):
        return self.subfolders
    
    def getParent(self):
        return self.parent

    def printNode(self, badding):    
        for i in self.files:
            print(badding," ", i[0], "    ", i[1])

        for i in self.subfolders:
            print(badding, "/", i.getName(), "   ", i.calculateFolderSize())
            i.printNode(badding + "--")

    def calculateFolderSize(self):
        sum = 0
        for i in self.files:
            sum += i[1]
        
        for i in self.subfolders:
            sum += i.calculateFolderSize()
        return sum

    

def printFolderStructure(rootNode):
    rootNode.printNode(badding = "")


def calculateFolders(folder, largestFolders):
    size = folder.calculateFolderSize()
    name = folder.getName()

    largestFolders.append((size, name))

    for i in folder.getSubFolders():
        calculateFolders(i, largestFolders)


def outputScraper(cmds, currentFolder):
    
    if cmds[0] == 'dir':
        currentFolder.addFolder(cmds[1])

    elif cmds[0].isnumeric():
        currentFolder.addFile(cmds[1], cmds[0])


def commandParser(line, currentFolder, root):

    cmds = line.split()
    #print(cmds)

    if cmds[0] == '$':
        if cmds[1] == 'cd':
            if cmds[2] == '/':
                currentFolder = root
                #print("change folder: root")
            elif cmds[2] == '..':
                if currentFolder.getParent() == None:
                    currentFolder = root
                else:
                    currentFolder = currentFolder.getParent()
            else:
                currentFolder = currentFolder.getSubFolder(cmds[2])
                

    else:
        outputScraper(cmds, currentFolder)

    return currentFolder


def main():

    largestFolders = []

    root = TreeNode("Root", None)
    currentFolder = root

    for x in data:
        currentFolder = commandParser(x, currentFolder, root)
        #print("current folder: ", currentFolder.getName())

    
    printFolderStructure(root)

    calculateFolders(root, largestFolders)
    largestFolders.sort(reverse=True)

    spaceLeft = 70000000 - largestFolders[0][0]
    spaceNeeded = abs(spaceLeft - 30000000)


    answerA = 0
    for i in largestFolders:
        #print(i)
        if i[0] < 100000:
            answerA += i[0]
    
    print("ANSWER A: ", answerA)


    largestFolders.sort()

    print("spaceleft: ", spaceLeft)
    print("spaceNeeded: ", spaceNeeded)

    answerB = 0
    for i in largestFolders:
        #print(i)
        if i[0] > spaceNeeded:
            answerB = i[0]
            break
    
    print("ANSWER B: ", answerB)




if __name__ == "__main__":
    main()


