import board
import displayio
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.roundrect import RoundRect
from adafruit_clue import clue

display = board.DISPLAY
clue_group = displayio.Group()

outer_circle = Circle(120, 120, 119, outline=clue.WHITE)
y_axis = RoundRect(80, 10, 80, 225, 10, outline=clue.RED, stroke=3)
x_axis = RoundRect(10, 80, 225, 80, 10, outline=clue.RED, stroke=3)
clue_group.append(outer_circle)
clue_group.append(x_axis)
clue_group.append(y_axis)

x, y, _ = clue.acceleration
bubble_groupx = displayio.Group()
bubble_groupy = displayio.Group()
level_bubblex = Circle(int(x + 120), int(y + 120), 20, fill=clue.RED, outline=clue.RED)
bubble_groupx.append(level_bubblex)

level_bubbley = Circle(int(x + 120), int(y + 120), 20, fill=clue.RED, outline=clue.RED)
bubble_groupy.append(level_bubbley)

clue_group.append(bubble_groupx)
clue_group.append(bubble_groupy)
display.show(clue_group)

while True:
    x, y, _ = clue.acceleration

    bubble_groupx.x = int(x * -10)
    bubble_groupy.y = int(y * -10)

    if (abs(x - 0) < 1.0):
        level_bubblex.outline=clue.GREEN
    else:
        level_bubblex.outline=clue.RED

    if (abs(y - 0) < 1.0):
        level_bubbley.outline=clue.GREEN
    else:
        level_bubbley.outline=clue.RED

    if (abs(x - 0)  < 0.5):
        x_axis.outline=clue.GREEN
        x_axis.fill=None
        level_bubblex.fill=clue.GREEN
    else:
        x_axis.outline=clue.RED
        x_axis.fill=None
        level_bubblex.fill=clue.RED

    if (abs(y - 0) < 0.5):
        y_axis.outline=clue.GREEN
        y_axis.fill=None
        level_bubbley.fill=clue.GREEN
    else:
        y_axis.outline=clue.RED
        y_axis.fill=None
        level_bubbley.fill=clue.RED
