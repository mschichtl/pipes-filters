from component import Component


class Pipe(Component):

    # init method
    def __init__(self, target: Component = None, value: int = 0, speed: int = 1):
        self.set_target(target)
        self.set_value(value)
        self.set_speed(speed)

    def to_text(self):
        return '--' + str(self.get_value()) + '--'
