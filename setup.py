from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(
    name='func_parallelizer',
    version='0.4.1',
    author='Vikash G',
    author_email='vikashgraja@gmail.com',
    description="Func_Parallelizer is a simple Python module for parallel execution of functions "
                "using multiprocessing. Ideal for parallel execution of heavy cpu operations",
    long_description=description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    project_urls={
        'PyPi Funding': 'https://donate.pypi.org',
        'Code': 'https://github.com/vikashgraja/Func_Parallelizer',
        'Pull requests': 'https://github.com/vikashgraja/Func_Parallelizer/pulls',
        'Issues': 'https://github.com/vikashgraja/Func_Parallelizer/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords='multiprocessing ',
    python_requires='>=3.6',
    zip_safe=False
)
