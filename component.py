from abc import ABCMeta, abstractmethod


class Component(metaclass=ABCMeta):

    # variable initiation
    target = None
    value = 0
    speed = 1

    # getter and setter methods
    def set_target(self, target: object = None):
        self.target = target

    def get_target(self):
        return self.target

    def set_value(self, value: int = 0):
        self.value = value

    def get_value(self):
        return self.value

    def set_speed(self, speed: int = 1):
        self.speed = speed

    def get_speed(self):
        return self.speed

    def add_value(self, value: int = 1):
        self.value += value

    # init method
    def __init__(self, target: object = None, value: int = 0, speed: int = 1):
        self.set_target(target)
        self.set_value(value)
        self.set_speed(speed)

    # custom methods
    def execute(self):
        if self.get_target() is not None\
                and self.get_value() > 0:
            if self.get_value() >= self.get_speed():
                self.get_target().add_value(self.get_speed())
                self.add_value(-self.get_speed())

    @abstractmethod
    def to_text(self):
        pass

    def update(self):
        self.execute()
