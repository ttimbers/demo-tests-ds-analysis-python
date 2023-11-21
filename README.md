# Demo of tests for functions used in data analysis

This repository serves as a demonstration of how to setup 
unit tests for functions that are used in a data analysis.
This is one step away from making a Python package.

The demo data analysis is shown here:
- `notebooks/eda.ipynb`

Those literate code documents call a function, `count_classes`, 
which lives in `src/count_classes.py`
and who calculates the number observations of each class of a data set.

The tests for `count_classes` live in `tests/test-count_classes.py`,
and the helper data for the tests lives in `tests/helper-count_classes.py`.

The test suite can be run via:

```
pytest tests/*
```

## Dependencies:
Jupyter, Python and the following packages:
- pandas
- pytest