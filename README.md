# Rabit

This project implement a simple API of turtle to draw line, rectangle, circle, text and convert the process into gif.



## Python Versions

python 3.

## Install

* Install the package.

```bash
pip3 install rabit
```

* Install ```python-tk```.

## Usage



## To create a Rabit object.

```python
import rabit

# The first argument is the number of grids in a row/column.
# The second argument is the size of the drawing board.
rabit = rabit.Rabit(11, 600)
```



The conversion can split into two steps:

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

## Examples

There is an example of drawing board in the example directory.

The converted gif is:

<img src="https://github.com/Ackeraa/turtle2gif/blob/master/example/heart.gif" alt="heart" style="zoom:66%;" />
