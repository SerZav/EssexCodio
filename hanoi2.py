""" Hanoi towers demonstration using recursion and memoization """

class Hanoi:
    """ main class for Hanoi towers """
    # variable initialization
    pegA = []
    pegB = []
    pegC = []
    memo = {}
    steps = 0
    disks = 0

    def __init__(self, disks):
        """ Constructor for the class """
        self.disks = disks
        for disk in range(disks, 0, -1):
            self.pegA.append(disk)

    def display_hanoi(self):
        """ Used if disks will be shown """
        self.arrange(self.disks, self.pegA, self.pegC, self.pegB)
        return self.steps

    def calculate_hanoi(self):
        """ method to calculate without showing the steps """
        total = self.calculate_only(self.disks, self.memo)
        return total

    def __str__(self):
        """ method to display the results """
        return f"peg A: {self.pegA}\npeg B: {self.pegB}\nPeg C: {self.pegC}\n--------"

    def arrange(self, step, move_from, aux, move_to):
        """ logic for disk arrangement """
        if step == 0:
            print(self)
            return
        self.steps += 1
        self.arrange(step - 1, move_from, move_to, aux)
        if move_from:
            move_to.append(move_from.pop())
        self.arrange(step - 1, aux, move_from, move_to)

    def calculate_only(self, step, dictionary):
        """ method for calculation only using memoization """
        if step < 2:
            return step
        if step in dictionary:
            return dictionary[step]
        newdictionary = 1 + self.calculate_only(step - 1, dictionary) + \
            self.calculate_only(step - 1, dictionary)
        dictionary[step] = newdictionary
        return dictionary[step]


if __name__ == "__main__":
    # Main program. Depending of the number of disks it will show the steps.
    # If number of disks is greater than 6, it will use a memoization approach to
    # optimize the number of steps.
    disk_input = int(input("Number of disks: "))
    tower = Hanoi(disk_input)
    if disk_input < 7:
        result = tower.display_hanoi()
        print(f"Total steps: {result}")
    elif disk_input > 998:
        print("Maximum amount exceeded")
    else:
        result = tower.calculate_hanoi()
        print("Skipping display. Using memoization:")
        print(f"Total steps: {result}")
