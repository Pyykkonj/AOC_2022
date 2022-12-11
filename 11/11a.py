
file = open("data.txt", "r")

data = file.read().splitlines()


class Monkey():
    def __init__(self, items, allMonkeys, operation, operationNumber, testNumber, testTrue, testFalse):
        self.items = items.copy()

        self.operation = operation
        self.operationNumber = operationNumber
        self.testNumber = testNumber
        self.testFalse = testFalse
        self.testTrue = testTrue

        self.allMonkeys = allMonkeys

    def addItem(self, item):
        self.items.append(item)

    def itemAmount(self):
        return len(self.items)
    
    def inspectItems(self):
        for i in range(0, len(self.items)):
            item = self.items.pop(0)
            self.inspectItem(item)

    def inspectItem(self, item):
        item = self.doOperation(item)

        item = int(item/3)

        self.doTest(item)

    def doOperation(self, item):

        if self.operationNumber == "old":
            calculus = item
        else:
            calculus = int(self.operationNumber)

        if self.operation == "*":
            return item*calculus
        elif self.operation == "+":
            return item+calculus

    def doTest(self, item):

        if item % self.testNumber == 0:
            self.allMonkeys[self.testTrue].addItem(item)
        else:
            self.allMonkeys[self.testFalse].addItem(item)

    def printMonkey(self):
        print("Items: ", self.items)
        print("Operation: new = old", self.operation, self.operationNumber)
        print("Test: divisible by ", self.testNumber)
        print("If true: throw ot monkey ", self.testTrue)
        print("If false: throw ot monkey ", self.testFalse, "\n")

    def printItems(self):
        print(self.items)


def main():

    allMonkeys = []

    rowCounter = 1


    items = []
    operation = "" 
    operationNumber = ""
    testNumber = ""
    testTrue = ""
    testFalse = ""

    for row in data:
        row = row.lstrip()
        cmd = row.split(" ")
        #print(row)

        if rowCounter == 1:
            pass

        if rowCounter == 2:
            items.clear()
            for i in range(2, len(cmd)):
                item = cmd[i].replace(',', '')
                #print("item: ", item)
                items.append(int(item))

        if rowCounter == 3:
            operation = cmd[4].strip()
            operationNumber = cmd[5]

        if rowCounter == 4:
            testNumber = int(cmd[3])

        if rowCounter == 5:
            testTrue = int(cmd[5])

        if rowCounter == 6:
            testFalse = int(cmd[5])

        if rowCounter == 7:
            allMonkeys.append(Monkey(items, allMonkeys, operation, operationNumber, testNumber, testTrue, testFalse))
        
        if rowCounter == 7:
            rowCounter = 1
        else:
            rowCounter += 1
    
    for i in range(0, len(allMonkeys)):
        print("Monkey: ", i)
        allMonkeys[i].printMonkey()


    monkeyInspectItemAmount = [0] * len(allMonkeys)

    for a in range(0, 20):
        for i in range(0, len(allMonkeys)):
            monkeyInspectItemAmount[i] += allMonkeys[i].itemAmount()
            allMonkeys[i].inspectItems()

    print("Items inspected: ", monkeyInspectItemAmount)

    monkeyInspectItemAmount.sort(reverse=True)

    print("Result: ", monkeyInspectItemAmount[0]*monkeyInspectItemAmount[1])



            



if __name__ == "__main__":
    main()


