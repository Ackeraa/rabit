# Turtle2Gif

This project is to convert python turtle drawing process to gif.



## Python Versions

python 3

## Install

* Install the package.

```bash
pip3 install turtle2gif
```

* Install ```python-tk```.

## Usage

The conversion can split into two steps:

* Capturing pictures at a certain rate while drawing.
* convert all pictures(.eps) into a gif by ```imageio```.

```python
from turtle2gif import turtle2gif
import turtle

def your_draw_function():
  ...

# The first argument is the name of your draw function.
# The second argument is the FPS(or rate) of the capturing process.
# The third argument is the FPS of the final gif.
turtle2gif.convert(your_draw_function, 10, 5)
```

## Examples

There is an example of drawing heart in the example directory.

The converted gif is:

<img src="/Users/gsx/MyProgram/Python/turtle2gif/example/heart.gif" alt="heart" style="zoom:66%;" />