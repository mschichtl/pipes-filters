class Pipe:
    target = None
    value = 0

    def __init__(self, target):
        self.set_target(target)

    def get_target(self):
        return self.target

    def set_target(self, target):
        self.target = target

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def add_value(self, value):
        self.value += value

    def push(self, value=1):
        self.add_value(value)

    def pop(self, value=1):
        self.target.push(value)
        self.add_value(-value)

    def render(self):
        print('--' + self.get_value() + '--')