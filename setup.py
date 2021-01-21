import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(name='turtle2gif',
      version='1.0',
      description='Convert turtle drawing process to gif.',
      url='http://github.com/ackeraa/turtle2gif',
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
