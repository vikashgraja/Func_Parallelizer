# func_parallelizer

Func_Parallelizer is a simple Python module for parallel execution of functions using multiprocessing. 

Ideal for parallel execution of heavy cpu operations like processing huge no of files in a directory or reading files for pandas.
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install func_parallelizer.

```bash
pip install func-parallelizer
```

## Usage
Import the required packages.

```python
from func_parallelizer import parallel_runner
```

Create a class that has your function and arguments.

If your function doesn't require any arguments you can skip this and directly add them in tasks.

```python
class task:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def this(self):
        consequences = do_this_with(self.arg1, self.arg2)
        return consequences

    def that(self):
        consequences = do_that_with(self.arg1, self.arg2)
        return consequences
```

Create objects using the above class.

```python
def do_nothing():
    print("Eat 5 Star")
    print("⭐⭐⭐⭐⭐")

do = task(arg1, arg2)
```

Make a list of tasks you have to do.

Note: Don't use parentheses for functions otherwise function will execute in this stage also.

```python
tasks = [
    do.this,
    do.that,
    do_nothing
]
```

Pass the tasks to the parallel_runner function

By default all cores are used but if you have life and want to do some other things, I would recommend to use 50% to 80% of your CPU cores.
```python
total_mayhem = parallel_runner(tasks, cpu_cores=2)
```
## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate. [GIT Repo](https://github.com/vikashgraja/Func_Parallelizer)

Feel free to ask any help(If it's about this package, dealing a lot IRL can't help yours too.)

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Code of Conduct

Everyone interacting in the readme_renderer project's codebases, issue trackers,
chat rooms, and mailing lists is expected to follow the [PSF Code of Conduct](https://github.com/pypa/.github/blob/main/CODE_OF_CONDUCT.md).

Copyright © 2014, [The Python Packaging Authority].