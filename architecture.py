import pipe
import filter
import time


class Architecture:

    start_node = None

    def get_start_node(self):
        return self.start_node

    def set_start_node(self, start_node):
        self.start_node = start_node

    def __init__(self, start_node=None):
        self.set_start_node(start_node)

    def get_components(self):
        components = []
        curr_node = self.get_start_node()

        while curr_node is not None:
            components.append(curr_node)
            curr_node = curr_node.get_target()

        return components

    def render(self):
        print(''.join(map(lambda x: x.to_text(), self.get_components())))

    def update(self):
        #map(lambda component: component.update(), self.get_components())
        for component in self.get_components()[::-1]:
            component.update()

    def launch(self):
        while True:
            self.render()
            self.update()
            time.sleep(0.5)