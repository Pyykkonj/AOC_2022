
file = open("data.txt", "r")

data = file.read().splitlines()


class Knot:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = [(x, y)]

    def move(self, dir):

        if dir == "U":
            self.y += 1
        elif dir == "D":
            self.y -= 1
        elif dir == "R":
            self.x += 1
        elif dir == "L":
            self.x -= 1
        else:
            return

        self.visited.append((self.x,self.y))   
    
    def getLocation(self):
        return (self.x, self.y)
    
    def getVisited(self):
        return self.visited


class Head(Knot):

    def __init__(self, x, y, Tail):
        super().__init__(x,y)
        self.tail = Tail

    def move(self, dir, n):

        for i in range(n):
            super().move(dir) 
            #print("Head pos: ", self.x, " ", self.y)      
            self.tail.moveTail(self.x, self.y, dir) 
        

class Tail(Knot):

    def __init__(self,x,y):
        super().__init__(x,y) 
    
    def moveTail(self, head_x, head_y, head_dir):

        if abs(head_x - self.x) > 1 or abs(head_y - self.y) > 1:
            if head_dir == "U":
                self.y = head_y-1
                self.x = head_x
            elif head_dir == "D":
                self.y = head_y+1
                self.x = head_x
            elif head_dir == "R":
                self.x = head_x-1
                self.y = head_y
            elif head_dir == "L":
                self.x = head_x+1
                self.y = head_y
            
            self.visited.append((self.x,self.y))  


        #print("Tail pos: ", self.x, " ", self.y)


def main():

    tail = Tail(0,0)
    head = Head(0,0, tail)
    
 
    for row in data:
        cmd = row.split(" ")

        direction = cmd[0]
        steps = int(cmd[1])

        #print("dir: ", direction, " n: ", steps)
        head.move(direction, steps)

    #print("Head visited locations: ", head.getVisited())
    #print("Tail visited locations: ", tail.getVisited())

    # Trim duplicates
    tailVisited = list(dict.fromkeys(tail.getVisited()))
    print("Tail visited location amount: ", len(tailVisited))


if __name__ == "__main__":
    main()


