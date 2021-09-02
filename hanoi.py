class Hanoi:
    pegA = []
    pegB = []
    pegC = []
    memo = {}
    steps = 0
    def __init__(self, disks):
        for disk in range(disks, 0, -1):
          self.pegA.append(disk)

    def displayHanoi(self):
        self.arrange(disks, self.pegA, self.pegC, self.pegB)
        return self.steps

    def calculateHanoi(self):
        result = self.calculateOnly(disks, self.memo)
        return result       

    def __str__(self):
        return (f"peg A: {self.pegA}\npeg B: {self.pegB}\nPeg C: {self.pegC}\n--------")

    def arrange(self, n, moveFrom, aux, moveTo):
        if n == 0:
            print(self)
            return            
        self.steps += 1
        self.arrange(n - 1, moveFrom, moveTo, aux)
        if moveFrom:
            moveTo.append(moveFrom.pop())
        self.arrange(n - 1, aux, moveFrom, moveTo)

    def calculateOnly(self, n, dictionary):
        if n < 2:
            return n
        if n in dictionary:
            return dictionary[n]
        newdictionary = 1 + self.calculateOnly(n - 1, dictionary) + self.calculateOnly(n - 1, dictionary)
        dictionary[n] = newdictionary
        return dictionary[n]


if __name__ == "__main__":
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





