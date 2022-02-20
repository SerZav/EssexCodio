""" Estimation test """
class Cocomo:
    """ Estimation for Cocomo method """
    effort = 0.0
    time = 0.0
    staff = 0.0
    selected_type = ""
    size = 0
    def __init__(self, kloc):
        self.size = kloc
        self.selected_type = self.get_type()
        if self.selected_type == "organic":
            a, b, c, d = self.organic()
        elif self.selected_type == "semi detached":
            a, b, c, d = self.semi_detached()
        elif self.selected_type == "embedded":
            a, b, c, d = self.embedded()
        self.effort = a * kloc ** b
        self.time =  c * self.effort **  d
        self.staff = self.effort / self.time

    @staticmethod
    def organic():
        """ Organic values """
        return (2.4, 1.05, 2.5, 0.38)

    @staticmethod
    def semi_detached():
        """ Semi Detached Values """
        return (3.0, 1.12, 2.5, 0.35)

    @staticmethod
    def embedded():
        """ Embedded values"""
        return (3.6, 1.20, 2.5, 0.32)

    def get_type(self):
        if self.size < 50:
            return "organic"
        elif self.size <= 300:
            return "semi detached"
        else:
            return "embedded"

    def __str__(self):
        return "Lines of code: " + str(self.size * 1000) + \
        "\nMode: " + self.selected_type + \
        "\nEffort: " + str(self.effort) + \
        "\nTime: " + str(self.time) + \
        "\nStaff: " + str(self.staff)

print(Cocomo(5))
print("-----")
print(Cocomo(150))
print("-----")
print(Cocomo(350))