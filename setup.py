from setuptools import setup, find_packages

def readme():
    with open('README.rst', 'r') as f:
        return f.read()
    
setup(
    name='pacflypy',
    version='0.1.1',
    description='PacflyPy is a Special Python Module',
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
    url='https://github.com/PacflyPy/PacflyPy',
    author='PacflyPy',
    author_email='pacflypy@pacflypy.com',
    license='MIT',
    packages=find_packages(where='src'),
    package_dir={'': 'src'}
)