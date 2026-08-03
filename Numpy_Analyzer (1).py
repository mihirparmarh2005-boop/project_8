"""
NumPy Analyzer
==============
A menu-driven toolkit that integrates NumPy functionality with
Object-Oriented Programming principles.

Author: (your name here)
"""

import numpy as np


class DataAnalytics:
    """
    Encapsulates array creation, manipulation, mathematical operations,
    searching/sorting/filtering, and statistical/aggregate computations
    on NumPy arrays.
    """

    # ------------------------------------------------------------------
    # Construction
    # ------------------------------------------------------------------
    def __init__(self, array: np.ndarray = None):
        """Constructor - initializes the analyzer, optionally with an array."""
        self.array = array

    # ------------------------------------------------------------------
    # Array Management: Creation
    # ------------------------------------------------------------------
    def create_array(self):
        """Interactively create a 1D, 2D, or 3D NumPy array."""
        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            size = int(input("\nEnter the number of elements: "))
            elements = self._read_elements(size, "1D array")
            self.array = np.array(elements)

        elif choice == "2":
            rows = int(input("\nEnter the number of rows: "))
            cols = int(input("Enter the number of columns: "))
            total = rows * cols
            elements = self._read_elements(total, "array")
            self.array = np.array(elements).reshape(rows, cols)

        elif choice == "3":
            depth = int(input("\nEnter the number of blocks (depth): "))
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))
            total = depth * rows * cols
            elements = self._read_elements(total, "array")
            self.array = np.array(elements).reshape(depth, rows, cols)

        else:
            print("Invalid choice. Returning to main menu.")
            return

        print("\nArray created successfully:")
        print(self.array)

    @staticmethod
    def _read_elements(count, label):
        """Private/static helper: reads `count` space-separated numbers from input."""
        raw = input(f"Enter {count} elements for the {label} separated by space: ")
        values = raw.strip().split()
        if len(values) != count:
            raise ValueError(f"Expected {count} elements, got {len(values)}.")
        return [float(v) if "." in v else int(v) for v in values]

    # ------------------------------------------------------------------
    # Array Management: Indexing & Slicing
    # ------------------------------------------------------------------
    def index_or_slice_menu(self):
        """Sub-menu offering indexing or slicing on the current array."""
        if not self._ensure_array_exists():
            return

        print("\nChoose an operation:")
        print("1. Indexing")
        print("2. Slicing")
        print("3. Go Back")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            self._do_indexing()
        elif choice == "2":
            self._do_slicing()
        elif choice == "3":
            return
        else:
            print("Invalid choice.")

    def _do_indexing(self):
        """Private method: access a specific element/row/column."""
        idx_str = input("Enter the index (e.g. 0 or 0,1): ").strip()
        try:
            if "," in idx_str:
                idx = tuple(int(i) for i in idx_str.split(","))
            else:
                idx = int(idx_str)
            print("\nIndexed Value:")
            print(self.array[idx])
        except (ValueError, IndexError) as e:
            print(f"Error: {e}")

    def _do_slicing(self):
        """Private method: slice rows and, for 2D+, columns."""
        try:
            row_range = input("Enter the row range (start:end): ").strip()
            r_start, r_end = self._parse_range(row_range)

            if self.array.ndim >= 2:
                col_range = input("Enter the column range (start:end): ").strip()
                c_start, c_end = self._parse_range(col_range)
                result = self.array[r_start:r_end, c_start:c_end]
            else:
                result = self.array[r_start:r_end]

            print("\nSliced Array:")
            print(result)
        except ValueError as e:
            print(f"Error: {e}")

    @staticmethod
    def _parse_range(range_str):
        """Private/static helper: parses 'start:end' into a tuple of ints."""
        start, end = range_str.split(":")
        return int(start), int(end)

    # ------------------------------------------------------------------
    # Mathematical Operations
    # ------------------------------------------------------------------
    def math_operations_menu(self):
        """Sub-menu for element-wise math, dot product, and matrix multiplication."""
        if not self._ensure_array_exists():
            return

        print("\nChoose a mathematical operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Dot Product (2D arrays)")
        print("6. Matrix Multiplication (2D arrays)")
        choice = input("Enter your choice: ").strip()

        if choice in {"1", "2", "3", "4"}:
            second = self._read_matching_array("Enter the same-size array elements")
            print("\nOriginal Array:")
            print(self.array)
            print("\nSecond Array:")
            print(second)

            if choice == "1":
                result = self._elementwise(second, "+")
                label = "Addition"
            elif choice == "2":
                result = self._elementwise(second, "-")
                label = "Subtraction"
            elif choice == "3":
                result = self._elementwise(second, "*")
                label = "Multiplication"
            else:
                result = self._elementwise(second, "/")
                label = "Division"

            print(f"\nResult of {label}:")
            print(result)

        elif choice == "5":
            second = self._read_matrix_like(self.array.shape)
            try:
                result = np.dot(self.array, second)
                print("\nDot Product:")
                print(result)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "6":
            rows = int(input("Enter the number of rows for the second array: "))
            cols = int(input("Enter the number of columns for the second array: "))
            elements = self._read_elements(rows * cols, "array")
            second = np.array(elements).reshape(rows, cols)
            try:
                result = np.matmul(self.array, second)
                print("\nMatrix Multiplication Result:")
                print(result)
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Invalid choice.")

    def _elementwise(self, other, op):
        """Private method: performs the requested element-wise operation."""
        if op == "+":
            return self.array + other
        if op == "-":
            return self.array - other
        if op == "*":
            return self.array * other
        if op == "/":
            return self.array / other
        raise ValueError("Unsupported operation")

    def _read_matching_array(self, prompt_label):
        """Private helper: reads an array with the same total size as self.array."""
        count = self.array.size
        raw = input(f"{prompt_label} ({count} elements separated by space): ")
        values = raw.strip().split()
        if len(values) != count:
            raise ValueError(f"Expected {count} elements, got {len(values)}.")
        nums = [float(v) if "." in v else int(v) for v in values]
        return np.array(nums).reshape(self.array.shape)

    def _read_matrix_like(self, shape):
        """Private helper: reads a 2D array shaped for a valid dot product."""
        rows, cols = shape[1], shape[0]
        print(f"(For a valid dot product, enter a {rows} x N array)")
        cols_in = int(input("Enter the number of columns: "))
        elements = self._read_elements(rows * cols_in, "array")
        return np.array(elements).reshape(rows, cols_in)

    # ------------------------------------------------------------------
    # Combine or Split Arrays
    # ------------------------------------------------------------------
    def combine_split_menu(self):
        """Sub-menu for combining two arrays or splitting the current one."""
        if not self._ensure_array_exists():
            return

        print("\nChoose an option:")
        print("1. Combine Arrays")
        print("2. Split Array")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            count = self.array.size
            raw = input(
                f"Enter the elements of another array to combine "
                f"({count} elements separated by space): "
            )
            values = raw.strip().split()
            if len(values) != count:
                print(f"Error: Expected {count} elements, got {len(values)}.")
                return
            nums = [float(v) if "." in v else int(v) for v in values]
            second = np.array(nums).reshape(self.array.shape)

            print("\nOriginal Array:")
            print(self.array)
            print("\nSecond Array:")
            print(second)

            combined = np.vstack((self.array, second))
            print("\nCombined Array (Vertical Stack):")
            print(combined)

        elif choice == "2":
            sections = int(input("Enter the number of sections to split into: "))
            try:
                parts = np.array_split(self.array, sections)
                print("\nOriginal Array:")
                print(self.array)
                print("\nSplit Result:")
                for i, part in enumerate(parts, start=1):
                    print(f"Part {i}:")
                    print(part)
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Invalid choice.")

    # ------------------------------------------------------------------
    # Search, Sort, and Filter
    # ------------------------------------------------------------------
    def search_sort_filter_menu(self):
        """Sub-menu for searching, sorting, and filtering the current array."""
        if not self._ensure_array_exists():
            return

        print("\nChoose an option:")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            value = float(input("Enter the value to search for: "))
            positions = np.argwhere(self.array == value)
            print("\nOriginal Array:")
            print(self.array)
            if positions.size == 0:
                print(f"\nValue {value} not found in the array.")
            else:
                print(f"\nValue {value} found at position(s):")
                print(positions.tolist())

        elif choice == "2":
            order = input("Sort ascending or descending? (a/d): ").strip().lower()
            print("\nOriginal Array:")
            print(self.array)
            sorted_arr = np.sort(self.array, axis=-1)
            if order == "d":
                sorted_arr = np.flip(sorted_arr, axis=-1)
            print("\nSorted Array:")
            print(sorted_arr)
            print("(Sorting applied row-wise.)")

        elif choice == "3":
            condition = input(
                "Enter a filter condition using 'x' (e.g. x > 20): "
            ).strip()
            try:
                x = self.array  # noqa: F841  (used inside eval)
                mask = eval(condition, {"x": x, "np": np})
                print("\nOriginal Array:")
                print(self.array)
                print("\nFiltered Values:")
                print(self.array[mask])
            except Exception as e:
                print(f"Error evaluating condition: {e}")
        else:
            print("Invalid choice.")

    # ------------------------------------------------------------------
    # Aggregates and Statistics
    # ------------------------------------------------------------------
    def aggregates_statistics_menu(self):
        """Sub-menu for aggregate and statistical computations."""
        if not self._ensure_array_exists():
            return

        print("\nChoose an aggregate/statistical operation:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        print("6. Minimum")
        print("7. Maximum")
        print("8. Percentile")
        print("9. Correlation coefficient (between this array and another)")
        choice = input("Enter your choice: ").strip()

        print("\nOriginal Array:")
        print(self.array)

        if choice == "1":
            print(f"\nSum of Array: {np.sum(self.array)}")
        elif choice == "2":
            print(f"\nMean of Array: {np.mean(self.array)}")
        elif choice == "3":
            print(f"\nMedian of Array: {np.median(self.array)}")
        elif choice == "4":
            print(f"\nStandard Deviation of Array: {np.std(self.array)}")
        elif choice == "5":
            print(f"\nVariance of Array: {np.var(self.array)}")
        elif choice == "6":
            print(f"\nMinimum Value: {np.min(self.array)}")
        elif choice == "7":
            print(f"\nMaximum Value: {np.max(self.array)}")
        elif choice == "8":
            p = float(input("Enter the percentile (0-100): "))
            print(f"\n{p}th Percentile: {np.percentile(self.array, p)}")
        elif choice == "9":
            count = self.array.size
            raw = input(
                f"Enter the elements of another array to correlate "
                f"({count} elements separated by space): "
            )
            values = raw.strip().split()
            if len(values) != count:
                print(f"Error: Expected {count} elements, got {len(values)}.")
                return
            nums = [float(v) for v in values]
            second = np.array(nums)
            corr = np.corrcoef(self.array.flatten(), second)[0, 1]
            print(f"\nCorrelation Coefficient: {corr}")
        else:
            print("Invalid choice.")

    # ------------------------------------------------------------------
    # Utility / class-level helpers
    # ------------------------------------------------------------------
    def _ensure_array_exists(self):
        """Private method: guards operations that require an existing array."""
        if self.array is None:
            print("\nNo array exists yet. Please create one first (Option 1).")
            return False
        return True

    @classmethod
    def from_list(cls, data):
        """Class method: build a DataAnalytics instance directly from a Python list."""
        return cls(np.array(data))

    @staticmethod
    def is_numeric_string(s):
        """Static method: utility to check whether a string represents a number."""
        try:
            float(s)
            return True
        except ValueError:
            return False


# ----------------------------------------------------------------------
# Menu-driven User Interface
# ----------------------------------------------------------------------
def main():
    analyzer = DataAnalytics()

    print("Welcome to the NumPy Analyzer!")
    print("=" * 40)

    while True:
        print("\nChoose an option:")
        print("1. Create a Numpy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                analyzer.create_array()
                # Optional immediate indexing/slicing, per Array Management spec
                follow_up = input(
                    "\nWould you like to index or slice this array now? (y/n): "
                ).strip().lower()
                if follow_up == "y":
                    analyzer.index_or_slice_menu()

            elif choice == "2":
                analyzer.math_operations_menu()

            elif choice == "3":
                analyzer.combine_split_menu()

            elif choice == "4":
                analyzer.search_sort_filter_menu()

            elif choice == "5":
                analyzer.aggregates_statistics_menu()

            elif choice == "6":
                print("\nThank you for using the NumPy Analyzer! Goodbye!")
                break

            else:
                print("\nInvalid choice. Please select a number between 1 and 6.")

        except Exception as e:
            print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    main()
