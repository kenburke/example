# Sorting Algorithms Homework

[![Build
Status](https://travis-ci.org/kenburke/sortingAlgorithms.svg?branch=master)](https://travis-ci.org/kenburke/sortingAlgorithms)

Example python project with continuous integration testing.

Examines bubblesort and quicksort complexity.

## usage

To use the package, first create a conda environment

```
conda env create
```

to install all dependencies outlined in `environment.yml`. Then activate the env

```
source activate sortingAlgorithms
```

Then the package's main function (located in `sortingComplexity/__main__.py`) 
can be run as follows

```
python -m sortingComplexity
```

or

```
bash ./RUNME.sh
```

## testing

Testing is as simple as running

```
python -m pytest
```

from the root directory of this project.

## interactive

This homework comes with a Jupiter notebook in `sortingAlgorithms.ipynb`.

It stores output plots describing complexity experiment results in `plots/`.
