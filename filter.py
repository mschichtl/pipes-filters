from component import Component


class Filter(Component):

    def __init__(self, target: Component = None, value: int = 0, speed: int = 1) -> object:
        Component.__init__(self, target, value, speed)

    def to_text(self):
        return '(' + str(self.get_value()) + ')'
