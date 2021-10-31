class Hanoi:
    pegA = []
    pegB = []
    pegC = []
    memo = {}
    steps = 0
    def __init__(self, disks):
        """ Constructor for the class """
        for disk in range(disks, 0, -1):
          self.pegA.append(disk)

    def displayHanoi(self):
        """ Used if disks will be shown """
        self.arrange(disks, self.pegA, self.pegC, self.pegB)
        return self.steps

    def calculateHanoi(self):
        """ method to calculate without showing the steps """
        result = self.calculateOnly(disks, self.memo)
        return result       

    def __str__(self):
        """ method to display the results """ 
        return (f"peg A: {self.pegA}\npeg B: {self.pegB}\nPeg C: {self.pegC}\n--------")

    def arrange(self, n, moveFrom, aux, moveTo):
        """ logic for disk arrangement """
        if n == 0:
            print(self)
            return            
        self.steps += 1
        self.arrange(n - 1, moveFrom, moveTo, aux)
        if moveFrom:
            moveTo.append(moveFrom.pop())
        self.arrange(n - 1, aux, moveFrom, moveTo)

    def calculateOnly(self, n, dictionary):
        """ method for calculation only using memoization """
        if n < 2:
            return n
        if n in dictionary:
            return dictionary[n]
        newdictionary = 1 + self.calculateOnly(n - 1, dictionary) + self.calculateOnly(n - 1, dictionary)
        dictionary[n] = newdictionary
        return dictionary[n]


if __name__ == "__main__":
    """ 
    Main program. Depending of the number of disks it will show the steps or not.
    If number of disks is greater than 6, it will use a memoization approach to
    optimize the number of steps.
    """
    disks = int(input("Number of disks: "))
    tower = Hanoi(disks)
    if disks < 7:
        result = tower.displayHanoi()
        print(f"Total steps: {result}")
    elif disks > 998:
        print("Maximum amount exceeded")
    else:
        result = tower.calculateHanoi()
        print("Skipping display. Using memoization:")
        print(f"Total steps: {result}")
