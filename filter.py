class Filter:

    # variable initiation
    target = None
    value = 0

    # getter and setter methods
    def get_target(self):
        return self.target

    def set_target(self, target):
        self.target = target

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    # init method
    def __init__(self, target=None):
        self.set_target(target)

    # custom methods
    def add_value(self, value):
        self.value += value

    def execute(self, value=1):
        if self.get_target() is not None\
                and self.get_value() > 0:
            self.get_target().add_value(value)
            self.add_value(-value)

    def to_text(self):
        return '(' + str(self.get_value()) + ')'

    def update(self):
        self.execute()