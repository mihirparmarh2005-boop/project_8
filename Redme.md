# NumPy Analyzer

A menu-driven Python command-line tool that combines **NumPy** array operations with **Object-Oriented Programming** principles. The project lets a user create, manipulate, analyze, and summarize NumPy arrays through a simple interactive console interface.

## Features

1. **Create a NumPy Array**
   - Create 1D, 2D, or 3D arrays by entering dimensions and elements.
2. **Array Management (Indexing & Slicing)**
   - Access individual elements or sub-arrays immediately after creating an array.
3. **Perform Mathematical Operations**
   - Element-wise addition, subtraction, multiplication, and division on two same-shaped arrays.
   - Dot product and matrix multiplication for 2D arrays.
4. **Combine or Split Arrays**
   - Combine two arrays with a vertical stack (`np.vstack`).
   - Split an array into a given number of sections (`np.array_split`).
5. **Search, Sort, or Filter Arrays**
   - Search for a value and return its position(s).
   - Sort the array (row-wise), ascending or descending.
   - Filter values using a custom condition (e.g. `x > 20`).
6. **Compute Aggregates and Statistics**
   - Sum, mean, median, standard deviation, variance, minimum, maximum, percentile, and correlation coefficient.
7. **Exit**
   - Cleanly exits the program.

## Project Structure

```
numpy-analyzer/
│
├── numpy_analyzer.py     # Main source code (DataAnalytics class + CLI menu)
└── README.md             # Project documentation (this file)
```

## Requirements

- Python 3.8+
- NumPy (`pip install numpy`)

## How to Run

```bash
python numpy_analyzer.py
```

Follow the on-screen menu prompts to create arrays and perform operations.

## Design Overview

All functionality is encapsulated inside a single `DataAnalytics` class:

- **Constructor (`__init__`)** — initializes the analyzer, optionally holding a NumPy array.
- **Private helper methods** (prefixed with `_`, e.g. `_do_indexing`, `_elementwise`, `_read_elements`) — internal logic not meant to be called directly from outside the class.
- **Public methods** (e.g. `create_array`, `math_operations_menu`, `aggregates_statistics_menu`) — expose each major feature and drive the corresponding sub-menu.
- **`@classmethod` `from_list`** — an alternate constructor that builds a `DataAnalytics` instance directly from a Python list.
- **`@staticmethod` `is_numeric_string`** — a utility method that doesn't depend on instance state.

The `main()` function implements the top-level menu loop and delegates each choice to the relevant `DataAnalytics` method, keeping the UI logic separate from the array-processing logic.

## Assumptions

Since the original requirements left some implementation details open, the following assumptions were made:

- **Sorting** is applied row-wise for 2D/3D arrays (there is no single well-defined order across an entire multi-dimensional array), with an ascending/descending choice.
- **Combining arrays** uses a vertical stack (`np.vstack`), which requires the two arrays to have the same number of columns. Both arrays must also match in overall shape when requested by the prompts.
- **Splitting** uses `np.array_split`, which allows splitting into a number of sections that doesn't have to evenly divide the array.
- **Filtering** accepts a Python-style boolean expression using `x` to represent the array (e.g. `x > 20`, `x % 2 == 0`), evaluated with NumPy's element-wise comparison.
- **Dot product / matrix multiplication** are offered in addition to the four basic element-wise operations, since the assignment's feature list explicitly calls out matrix multiplication as a requirement.
- **Percentile and correlation coefficient** were added to the aggregates/statistics menu beyond the four basic stats shown in the example transcript, to fully satisfy the "aggregate and statistical operations" requirement in the spec.
- Numeric input is parsed as `int` unless a decimal point is present, in which case it is parsed as `float`.
- Basic input validation and error handling (e.g. mismatched element counts, invalid indices, division errors) is done with `try/except` blocks so the program doesn't crash on bad input — it reports the error and returns to the menu.

## Author

(your name here)

## License

This project was created for academic/assessment purposes.
