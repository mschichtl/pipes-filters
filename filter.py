class Filter:

    # variable initiation
    target = None
    value = 0
    speed = 1

    # getter and setter methods
    def get_target(self):
        return self.target

    def set_target(self, target):
        self.target = target

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed

    # init method
    def __init__(self, target=None, speed=1):
        self.set_target(target)
        self.set_speed(speed)

    # custom methods
    def add_value(self, value):
        self.value += value

    def execute(self):
        if self.get_target() is not None\
                and self.get_value() > 0:
            if self.get_value() >= self.get_speed():
                self.get_target().add_value(self.get_speed())
                self.add_value(-self.get_speed())

    def to_text(self):
        return '(' + str(self.get_value()) + ')'

    def update(self):
        self.execute()