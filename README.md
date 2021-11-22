# Rabit

This project implements a simple API of turtle to draw line, rectangle, circle, text and convert the process into gif.

## Install

* Install the package.

```bash
pip3 install rabit
```

* Install ```python-tk```.

## Usage

Rabit splits the drawing board into grids x grids. To create a Rabit object, you should choose the grids (in a row/column) you want to split and the size(default is 600) of drawing board.

```python
import rabit

# The first argument is the number of grids in a row/column.
# The second argument is the size of the drawing board.
rabit = rabit.Rabit(11, 600)
```

You can draw rectangle with ``draw_rect(row, col, rows=1, cols=1, color="black")``.

* ``row``: row of the left up corner of the rectangle
* ``col``: column of the left up corner of the rectangle
* ``rows``: length of the rectangle
* ``cols``: width of the rectangle
* ``color``: line color

You can paint rectangle with ``paint_rect(row, col, rows=1, cols=1, color="black", cover=Flase)``.

* ``row``: row of the left up corner of the rectangle
* ``col``: column of the left up corner of the rectangle
* ``rows``: length of the rectangle
* ``cols``: width of the rectangle
* ``color``: line color
* ``cover``: if cover the text on it 

You can clear rectangle with ``clear_rect(row, col, rows=1, cols=1, color="white")``.

* ``row``: row of the left up corner of the rectangle
* ``col``: column of the left up corner of the rectangle
* ``rows``: length of the rectangle
* ``cols``: width of the rectangle
* ``color``: line color

You can draw text with ``draw_text(row, col, text, color="black", font=("Times", 24))``.

* ``row``: row of the text
* ``col``: column of text
* ``text``: text
* ``color``: text color
* ``font``: text font

You can draw line with ``draw_line(from_row, from_col, to_row, to_col, color="black") ``.

* ``from_row``: row of start point
* ``from_col``: column of start point
* ``to_row``: row of end point
* ``to_col``: column of end point
* ``color``: line color

You can convert the drawing process into gif with ``convert2gif(func, fps_for_eps, fps_for_gif)``.The conversion can split into two steps:

* Capturing pictures at a certain rate while drawing.
* convert all pictures(.eps) into a gif at a certain FPS by ```imageio```.

```python
import rabit

def your_draw_function():
  ...

# The first argument is the name of your draw function.
# The second argument is the FPS(or rate) of the capturing process.
# The third argument is the FPS of the final gif.
rabit.convert2gif(your_draw_function, 10, 5)
```

There are other functions you can use:

* ``speed(speed)``: set the drawing speed
* ``delay(time)``: set the delay time(ms)
* ``pensize(pensize)``: set the pensize
* ``begin_hide()``: hide the following drawing animation
* ``end_hide()``: end of the hiding
* ``hold()``: don't close the window after the drawing

## Examples

There is an example in the example directory.

The converted gif is:

<img src="https://github.com/Ackeraa/rabit/blob/master/example/example.gif" alt="example" style="zoom:66%;" />
