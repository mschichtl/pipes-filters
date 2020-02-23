from architecture import Architecture
from pipe import Pipe
from filter import Filter

arc = Architecture()

f1 = Filter(speed=3)
f2 = Filter()
f3 = Filter()

p1 = Pipe(speed=2)
p2 = Pipe()

f1.set_target(p1)
p1.set_target(f2)
f2.set_target(p2)
p2.set_target(f3)

f1.set_value(10)

arc.set_start_node(f1)

arc.launch()