"""
func_parallelizer Module

This module provides a function which can be used to run tasks in parallel
(even if they return values)

Usage:
    - Import the module: `from func_parallelizer import parallel_runner`
    - Create a list of tasks with their arguments.
    - pass the list to the parallel_runner.

"""

import multiprocessing as mp

all_cores = mp.cpu_count()

def execute(func):
    """
    Executes a given function with its arguments.

    Parameters
    ----------
    func : function to execute

    Returns
    -------
    What the passed function returns

    """
    return func()


def parallel_runner(tasks, cpu_cores=all_cores):
    """
    Runs tasks in parallel using multiprocessing.

    Parameters
    ----------
    tasks : list
    cpu_cores : no of cpu cores
    """
    with mp.Pool(processes=cpu_cores) as pool:
        returns = pool.map(execute,[task for task in tasks])
    pool.join()
    return returns
