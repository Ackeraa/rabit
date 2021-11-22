import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(name='rabit',
      version='0.3',
      description='This project implements a simple API of turtle to draw line, rectangle, circle, text and convert the process into gif.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='http://github.com/ackeraa/rabit',
      author='Acker',
      author_email='acker2880@gmail.com',
      license='MIT',
      packages=setuptools.find_packages(),
      install_requires=[
          'pythonturtle',
          'imageio'
      ],
      include_package_data = True,
      platforms = 'any',
      python_requires='>=3.6'
 )
