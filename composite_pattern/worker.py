class Worker:

    def __init__(self, name, title, happiness_percent):
        self.name = name
        self.title = title
        self.happiness_percent = happiness_percent

    def display_status(self):
        print(
            f'{self.title} {self.name} shows hapiness level of {self.happiness_percent} percent.')
