import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(name='rabit',
      version='0.1',
      description='Drawing arrays with turtle.',
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
