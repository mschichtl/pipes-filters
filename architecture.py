import pipe
import filter


class Architecture:

    start_node = None

    def get_start_node(self):
        return self.start_node

    def set_start_node(self, start_node):
        self.start_node = start_node

    def __init__(self, start_node=None):
        self.set_start_node(start_node)

    def render(self):
        display_string = ""
        curr_node = self.get_start_node()

        while curr_node is not None:
            display_string += str(curr_node.render())
            curr_node = curr_node.get_target()

        print(display_string)