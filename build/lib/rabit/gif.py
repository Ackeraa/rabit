import turtle
import imageio
import os
import sys
import glob
import shutil
import re

class Gif(object):
    def __init__(self, func, fps_for_eps, fps_for_gif):
        self.__func = func
        self.__running = True
        self.__fps_for_eps = fps_for_eps
        self.__fps_for_gif = fps_for_gif
        self.__cnt = 1
        save_name = './' + sys.argv[0][:-3] + '.gif'
        if not os.path.exists('tmp'):
            os.mkdir('tmp')

    # sort *.eps files by numerical order.
    def __numericalSort(self, value):
        parts = re.compile(r'(\d+)').split(value)
        parts[1::2] = map(int, parts[1::2])
        return parts

    def __draw(self):
        turtle.hideturtle()
        self.__func()
        turtle.ontimer(self.__stop, 500)
        turtle.down()

    def __stop(self):
        self.__running = False

    # save to temporary .eps files
    def __save(self):
        print('  Capturing picture %04d.' % self.__cnt)
        turtle.getcanvas().postscript(file = "./tmp/{0:04d}.eps".format(self.__cnt))
        self.__cnt += 1
        if self.__running:
            turtle.ontimer(self.__save, int(1000 / self.__fps_for_eps))
        else:
            turtle.ontimer(self.__convert, 500)

    def __convert(self):
        turtle.bye()
        print('Finished drawing and capturing.')
        print('Begin to convert the captured eps files to gif...')
        # read .eps files and change them to gif.
        images = []
        for file in sorted(glob.glob('./tmp/*.eps'), key=self.__numericalSort):
            images.append(imageio.imread(file))
        kwargs_write = {'fps': self.__fps_for_gif, 'quantizer': 'nq'}
        save_name = './' + sys.argv[0][:-3] + '.gif'
        imageio.mimsave(save_name, images, 'GIF-FI', **kwargs_write)
        shutil.rmtree('./tmp')
        print('Finished converting, have fun!')

    def run(self):
        print('Begin to draw and Capturing pictures...')
        self.__save()
        turtle.ontimer(self.__draw, 500)
        turtle.done()

def convert2gif(func, fps_for_eps=10, fps_for_gif=10):
    gif = Gif(func, fps_for_eps, fps_for_gif)
    gif.run()
