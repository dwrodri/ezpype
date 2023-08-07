# ezpype

⚠️**DISCLAIMER: EZPype is a toy project updated at my own leisure for my own personal use. DO NOT USE IN PRODUCTION**⚠️

EZPype is a simple, easy-to-use, easy-to-read library for building reproducible data transformations in Python.

EZPype is inspired by [scikit learn](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html), [PyTorch's DataLoader](https://pytorch.org/docs/stable/data.html), and [this Tweet by @svpino](https://twitter.com/svpino/status/1688201830285611008).

## What problem does EZPype solve?

I often find myself using a mix of shell scripts and short Python scripts to
prepare "draft" datasets for testing things out, only to later realize that I
might forget how I took those 100s of GBs of data and created the thing I'm
using as a baseline for my entire ML pipeline. **The goal of EZPype is to 
provide so much convenience that you'll reach for EZPype instead of doing
everything in the CLI like I do currently**.

EZPype provides a hackable interface that gets your data preprocessing from nothing to immmediately
having the following features:
- Checkpointing
- Logging
- Reproducibility
- Portability (Pure Python by default!)
- `multiprocessing` friendly concurrency


## Goals

- Easily extensible w/ good support for optional dependencies(Pandas/NumPy/Parquet/Logging)
- Beginner-friendly, pure Python codebase with lots of documentation
- Provide lots of visibility

## Non Goals

- Ultra high-performance
- “Production Hardened” - This is just a little hobby product to practice Python software engineering skills
- Async-friendly

Here's an example of how to use EZPype:
```python
from EZPype import Pipeline
from EZPype.reports import SimpleStats
from typing import List
import multiprocessing
import sys

# write your python code to parse the data as you wish
def filter_numbers(sample_line:str) -> List[int]:
    return [int(x) for x in sample_line.split(",") if all(char.isdigit() for char in x)]

def only_odds(entry: List[int]) -> List[int]:
    return [x for x in entry if x%2 == 0]

# add a 

# Create a pipeline and add your transforms in order, appended with an aggregator

pipeline = Pipeline("find_odds_in_csv", stages=[filter_numbers, only_odds]) | SimpleStats()

# consume files in parallel in a pool, 
input_files = sys.argv[1:]
with multiprocessing.Pool() as p:
    results = p.map(pipeline.processTextFile, input_files)
```